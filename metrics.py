from prometheus_client import Counter, Gauge, Info

metrics = {
    "data_feed": Gauge("data_feed", "Numeric data feed", ["project", "code"]),
    "data_feed_response_time_ms": Gauge(
        "data_feed_response_time",
        "Response time of data feed in milliseconds",
        ["project", "code"],
    ),
    "data_feed_last_error": Info(
        "data_feed_last_error", "Most recent error detected", [
            "project", "code"]
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

    "fluxmon_decimals": Gauge("fluxmon_decimals", "Decimals of reported value", ["project", "code"]),
    "fluxmon_allocated_funds": Gauge(
        "fluxmon_allocated_funds",
        "Allocated funds",
        ["project", "code"],
    ),
    "fluxmon_available_funds": Gauge(
        "fluxmon_available_funds",
        "Available funds",
        ["project", "code"],
    ),
    "fluxmon_latest_answer": Gauge(
        "fluxmon_latest_answer",
        "Lastest answer",
        ["project", "code"],
    ),
    "fluxmon_latest_round": Gauge(
        "fluxmon_latest_round",
        "Lastest round",
        ["project", "code"],
    ),
    "fluxmon_withdrawable_payment": Gauge(
        "fluxmon_withdrawable_payment",
        "Withdrawable payment",
        ["project", "code"],
    ),

}


def init_metrics(cfg):
    for data_feed_source in cfg["data_source_metrics"]:
        metrics["data_feed"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).set(0)
        metrics["data_feed_response_time_ms"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).set(0)
        metrics["data_feed_last_error"].labels(
            data_feed_source["project"], data_feed_source["code"]
        ).info({"status": "", "timestamp": "", "error": ""})
    for fluxmon_contract in cfg["fluxmon_contracts"]:
        for metric in ["fluxmon_decimals", "fluxmon_allocated_funds", "fluxmon_available_funds", "fluxmon_latest_answer", "fluxmon_latest_round", "fluxmon_withdrawable_payment"]:
            metrics[metric].labels(
                fluxmon_contract["project"], fluxmon_contract["code"]
            ).set(0)
        print(
            f"Initialised metrics for {data_feed_source['project']}-{data_feed_source['code']}",
        )
