// SPDX-License-Identifier: GPL-3.0

// Solidity program to
// retrieve address and
// balance of owner
pragma solidity >=0.6.8;

// Creating a contract
contract OwnerSmartContract {
    // Private state variable
    address private owner;
    // Keep track of the funders and the amount funded
    mapping(address => uint256) public funderToAmount;
    // List to keep track of funders, since we can't iterate through mapping
    address[] funders;

    // Defining a constructor
    constructor() {
        owner = msg.sender;
    }

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Fallback function is called when msg.data is not empty
    fallback() external payable {}

    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }

    // Modifier if function requires the owner and only him.
    modifier onlyOwner() {
        require(owner == msg.sender, "Ownable: caller is not the owner");
        _;
    }

    // Extract some eth from the contract for yourself
    function extractEth(uint256 amount) public payable onlyOwner {
        sendEth(payable(msg.sender), amount);
    }

    // Send eth to someone
    function sendEth(address payable recipient, uint256 amount)
        public
        payable
        onlyOwner
    {
        // https://solidity-by-example.org/sending-ether/
        // Send returns a boolean value indicating success or failure.
        // This function is not recommended for sending Ether.
        // bool sent = _to.send(msg.value);
        // require(sent, "Failed to send Ether");
        recipient.transfer(amount);
    }

    // Function to get address of owner
    function getOwner() public view returns (address) {
        return owner;
    }

    // Function to return current balance of owner
    function getBalance() public view returns (uint256) {
        return owner.balance;
    }

    // Function to send some eth officially
    function fundEth() public payable {
        require(msg.value > 0, "You need to fund more than 0 eth.");
        funderToAmount[msg.sender] += msg.value;
        // TODO: You have to remove duplicates though
        funders.push(msg.sender);
    }

    function getAllfunders() public view returns (address[] memory) {
        return funders;
    }
}
