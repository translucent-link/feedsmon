from web3 import Web3


def analyse_contracts(cfg, contracts):
    for contract in contracts:
        rpc_for_contract = cfg[contract["network"]]
        w3 = Web3(Web3.HTTPProvider(rpc_for_contract))

        if w3.is_connected():
            print(f"Connected to {contract['network']}")
            contract_instance = w3.eth.contract(contract["address"], abi=cfg["abi"])
            allocated_funds = contract_instance.functions.allocatedFunds().call()
            available_funds = contract_instance.functions.availableFunds().call()
            decimals = contract_instance.functions.decimals().call()
            latest_answer = contract_instance.functions.latest_answer().call()
            latest_round = contract_instance.functions.latest_round().call()
            withdrawable_payment = (
                contract_instance.functions.withdrawablePayment().call()
            )
        else:
            print(f"Failed to connect to {contract['network']}")
