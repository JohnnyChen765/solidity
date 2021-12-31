from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import Wei, network, accounts, exceptions
import pytest


# def test_can_fund_and_withdraw():
#     account = get_account()
#     fund_me = deploy_fund_me()
#     entrance_fee = fund_me.getEntranceFee() + 100
#     tx = fund_me.fund({"from": account, "value": entrance_fee})
#     tx.wait(1)
#     assert fund_me.addressToAmountFunded(account.address) == entrance_fee
#     tx2 = fund_me.withdraw({"from": account})
#     tx2.wait(1)
#     assert fund_me.addressToAmountFunded(account.address) == 0


def test_fund_fails_if_not_enough():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = Wei("0.1 ether")

    tx = fund_me.fund(
        {
            "from": account,
            "value": entrance_fee,
            "base_fee": "100 gwei",
            "priority_fee": "100 gwei",
            "max_fee": "500 gwei",
        }
    )
    tx.wait(1)
    tx.call_trace()
    import ipdb

    ipdb.set_trace()


# def test_only_owner_can_withdraw():
#     if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         pytest.skip("only for local testing")
#     fund_me = deploy_fund_me()
#     bad_actor = accounts.add()
#     with pytest.raises(exceptions.VirtualMachineError):
#         fund_me.withdraw({"from": bad_actor})
