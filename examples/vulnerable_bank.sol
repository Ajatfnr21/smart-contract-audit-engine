// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VulnerableBank {
    mapping(address => uint) public balances;
    
    // VULNERABLE: Reentrancy
    function withdraw() public {
        uint amount = balances[msg.sender];
        require(amount > 0);
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success);
        
        balances[msg.sender] = 0;
    }
    
    // VULNERABLE: Tx.Origin
    function transfer(address to, uint amount) public {
        require(tx.origin == msg.sender);
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }
    
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
}
