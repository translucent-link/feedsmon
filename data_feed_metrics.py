from prometheus_client import Counter, Gauge, Info, start_http_server

metrics = {
    "data_feed": Gauge("data_feed", "Numeric data feed", ["project", "code"]),
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
