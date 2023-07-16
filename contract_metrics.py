from web3 import Web3
from cfg import network, flux_monitor_abi

from metrics import metrics


def analyse_fluxmon_contracts(cfg, contracts):
    print(f"Analysing {len(contracts)} contracts...")
    for contract in contracts:
        print(
            f"Analysing contract {contract['code']} on {contract['network']}")
        chain = network(cfg['general']['networks'], contract['network'])
        if network is not None:
            w3 = Web3(Web3.HTTPProvider(chain["rpc"]))

            if w3.is_connected():
                contract_instance = w3.eth.contract(
                    contract["address"], abi=flux_monitor_abi)
                decimals = contract_instance.functions.decimals().call()
                allocated_funds = contract_instance.functions.allocatedFunds().call() / 10 ** 18
                available_funds = contract_instance.functions.availableFunds().call() / 10 ** 18
                latest_answer = contract_instance.functions.latestAnswer().call() / 10 ** 18
                latest_round = contract_instance.functions.latestRound().call()
                withdrawable_payment = (
                    contract_instance.functions.withdrawablePayment(
                        contract['oracle_address']).call()
                ) / 10 ** 18

                metrics["fluxmon_decimals"].labels(
                    contract["project"], contract["code"]
                ).set(decimals)
                metrics["fluxmon_allocated_funds"].labels(
                    contract["project"], contract["code"]
                ).set(allocated_funds)
                metrics["fluxmon_available_funds"].labels(
                    contract["project"], contract["code"]
                ).set(available_funds)
                metrics["fluxmon_latest_answer"].labels(
                    contract["project"], contract["code"]
                ).set(latest_answer)
                metrics["fluxmon_latest_round"].labels(
                    contract["project"], contract["code"]
                ).set(latest_round)
                metrics["fluxmon_withdrawable_payment"].labels(
                    contract["project"], contract["code"]
                ).set(withdrawable_payment)

            else:
                print(f"Failed to connect to {contract['network']}")
        else:
            print(f"Network {contract['network']} not found in config")
