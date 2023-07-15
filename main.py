import time

from prometheus_client import start_http_server

from cfg import load_config
from data_feed_metrics import analyse_data_feeds, init_metrics

if __name__ == "__main__":
    start_http_server(8000)
    data_feed_sources = load_config()
    init_metrics(data_feed_sources)
    while True:
        analyse_data_feeds(data_feed_sources)
        time.sleep(60)
