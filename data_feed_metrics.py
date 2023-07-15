import datetime

import pyjq
import requests
from prometheus_client import Counter, Gauge, Info

metrics = {
    "data_feed": Gauge("data_feed", "Numeric data feed", ["project", "code"]),
    "data_feed_response_time_ms": Gauge(
        "data_feed_response_time",
        "Response time of data feed in milliseconds",
        ["project", "code"],
    ),
    "data_feed_last_error": Info(
        "data_feed_last_error", "Most recent error detected", ["project", "code"]
    ),
    "data_feed_error_count": Counter(
        "data_feed_error_count",
        "Number of errors whilst retrieving data feed",
        ["project", "code"],
    ),
    "data_feed_update_count": Counter(
        "data_feed_update_count",
        "Number of times data feed retrieved",
        ["project", "code"],
    ),
}


def init_metrics(data_feed_sources):
    for data_feed_source in data_feed_sources["data_source_metrics"]:
        metrics["data_feed"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).set(0)
        metrics["data_feed_response_time_ms"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).set(0)
        metrics["data_feed_last_error"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).info({"status": "", "timestamp": "", "error": ""})
        print(
            f"Initialised metrics for {data_feed_source['project']}-{data_feed_source['code']}",
        )


def analyse_data_feeds(data_feed_sources):
    for data_feed_source in data_feed_sources["data_source_metrics"]:
        try:
            request_datetime = datetime.datetime.now()
            response = requests.get(
                data_feed_source["url"], headers=data_feed_source["headers"]
            )
            current_datetime = datetime.datetime.now()
            if response.status_code != 200:
                metrics["data_feed_last_error"].labels(
                    data_feed_source["project"], data_feed_source["code"]
                ).info(
                    {
                        "status": response.status_code,
                        "timestamp": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                        "error": response.text,
                    }
                )
                metrics["data_feed_error_count"].labels(
                    data_feed_source["project"], data_feed_source["code"]
                ).inc()
            else:
                data = response.json()
                duration = (current_datetime - request_datetime).total_seconds() * 1000
                metrics["data_feed_response_time_ms"].labels(
                    data_feed_source["project"], data_feed_source["code"]
                ).set(duration)
                price_str = pyjq.first(data_feed_source["jq"], data)
                price = float(price_str) / 10 ** data_feed_source["decimals"]
                metrics["data_feed"].labels(
                    data_feed_source["project"], data_feed_source["code"]
                ).set(price)
                metrics["data_feed_update_count"].labels(
                    data_feed_source["project"], data_feed_source["code"]
                ).inc()
            print(f"{data_feed_source['code']} price: {price}")

        except Exception as e:
            current_datetime = datetime.datetime.now()
            metrics["data_feed_last_error"].labels(
                data_feed_source["project"], data_feed_source["code"]
            ).info(
                {
                    "status": "0",
                    "timestamp": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    "error": f"{e.args[0]}",
                }
            )
            metrics["data_feed_error_count"].labels(
                data_feed_source["project"], data_feed_source["code"]
            ).inc()
