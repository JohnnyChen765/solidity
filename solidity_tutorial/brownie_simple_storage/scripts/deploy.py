from brownie import accounts, config, SimpleStorage, network

# To import a compiled contract from build, just import as a module/package


def deploy_simple_storage():
    # brownie run scripts/ will always spin a local ganache --accounts 10 etc if no network provided
    account = get_account()
    # No need to specify call, transact, and the nonce
    # When changing states, we have to specify from ?
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # How many blocks we wanna wait
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        # Get the first account of the 10 accounts spinned locally by Ganache
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
