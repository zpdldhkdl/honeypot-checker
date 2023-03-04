from web3 import Web3
from dotenv import load_dotenv
import os
from honeypot_checker_caller import HoneyPotCheckerCaller
from constants.config import CONFIG
from constants.abi import SIMPLE_BEP20

if __name__ == "__main__":
    load_dotenv()
    launch_environment = os.environ.get("LAUNCH_ENVIRONMENT")
    if not launch_environment:
        exit()

    config = CONFIG[launch_environment]
    rpc = config.get("RPC")
    contract_address = config.get("HONEYPOT_CHECKER_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(rpc))
    honeypot_checker_caller = HoneyPotCheckerCaller(
        web3=w3,
        contract_address=contract_address
    )

    router_address = config.get("PANCAKE_SWAP_ROUTER_ADDRESS")

    base_token_address = config.get("WBNB_ADDRESS")
    target_token_address = w3.toChecksumAddress(
        "0x55d398326f99059ff775485246999027b3197955")

    path = [base_token_address, target_token_address]

    check_result = honeypot_checker_caller.check(
        router_address, path=path)

    if check_result is None:
        exit()

    buy_gas, sell_gas, estimated_buy, exact_buy, estimated_sell, exact_sell = check_result

    buy_tax = honeypot_checker_caller.calculate_tax_fee(
        estimated_buy, exact_buy)
    sell_tax = honeypot_checker_caller.calculate_tax_fee(
        estimated_sell, exact_sell)

    # get symbol & token name
    target_token_contract = w3.eth.contract(
        address=target_token_address,
        abi=SIMPLE_BEP20
    )

    target_token_name = target_token_contract.caller().name()
    target_token_symbol = target_token_contract.caller().symbol()

    print(f"""
          ===============================================
                      name: {target_token_name}
                    symbol: {target_token_symbol}
          used gas for buy: {buy_gas}
                  for sell: {sell_gas}
               buy tax fee: {buy_tax} %
              sell tax fee: {sell_tax} %
          ===============================================
          """)
