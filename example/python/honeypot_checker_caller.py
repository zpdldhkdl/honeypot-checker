from web3 import Web3
from constants.abi import HONEYPOT_CHECKER_ABI


class HoneyPotCheckerCaller:
    def __init__(self, web3: Web3, contract_address) -> None:
        self.web3 = web3

        self.gas_limit = 4_000_000
        self.gas_price = self.web3.toWei("10", "gwei")
        self.value = self.web3.toWei("1", "ether")

        self.honeypot_checker_contract = web3.eth.contract(
            address=contract_address,
            abi=HONEYPOT_CHECKER_ABI
        )

    def check(self, router_address, path):
        try:
            result = self.honeypot_checker_contract.functions.check(
                router_address, path
            ).call({
                "gasLimit": self.gas_limit,
                "gasPrice": self.gas_price,
                "value": self.value
            })

            return result
        except:
            print("honeypot or lp doesn't exist")
            return None

    def calculate_tax_fee(self, estimated_price, exact_price):
        result = round(
            ((estimated_price - exact_price) / estimated_price) * 100, 1)

        return 0 if result <= 0 else result
