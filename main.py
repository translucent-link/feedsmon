import time

from prometheus_client import start_http_server

from cfg import load_config
from contract_metrics import analyse_fluxmon_contracts
from metrics import init_metrics
from data_feed_metrics import analyse_data_feeds

if __name__ == "__main__":
    start_http_server(8000)
    config = load_config()
    init_metrics(config)
    while True:
        analyse_data_feeds(config)
        analyse_fluxmon_contracts(config, config['fluxmon_contracts'])
        time.sleep(60)
