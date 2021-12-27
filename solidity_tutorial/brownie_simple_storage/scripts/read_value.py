from brownie import SimpleStorage, accounts, config


def read_contract():
    # Get always the most recent deployment of the contract
    # When interacting with a contract, we always need:
    # - ABI
    # - contract address
    # Brownlie already saved those in build/deployments/
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
