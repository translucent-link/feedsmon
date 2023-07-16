from yaml import load
import os

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_config():

    cfg_path = os.environ.get("FEEDSMON_CONFIG")
    if cfg_path is None:
        cfg_path = "./feedsmon.yml"

    with open(cfg_path, "r") as f:
        return load(f, Loader=Loader)


def network(networks, network_code):
    for netw in networks:
        if netw["code"] == network_code:
            return netw
    return None


flux_monitor_abi = [{"inputs": [], "name":"allocatedFunds", "outputs":[{"internalType": "uint128", "name": "", "type": "uint128"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"availableFunds", "outputs":[{"internalType": "uint128", "name": "", "type": "uint128"}], "stateMutability": "view", "type": "function"},  {"inputs": [], "name":"decimals", "outputs":[{"internalType": "uint8", "name": "", "type": "uint8"}], "stateMutability": "view", "type": "function"}, {"inputs": [
], "name":"latestAnswer", "outputs":[{"internalType": "int256", "name": "", "type": "int256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"latestRound", "outputs":[{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_oracle", "type": "address"}], "name": "withdrawablePayment", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}]
