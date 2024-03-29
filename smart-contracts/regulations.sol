// SPDX-License-Identifier: GPL-3.0 specifies the license for the Solidity code

// The pragma directive specifies the version of Solidity to be used for the contract
pragma solidity >=0.8.2 <0.9.0;

// Regulation contract that can be deployed by a government, creates new standard
contract Regulations{

    struct Standard{
        address government;
        string standard_name;
        string description;        
    }

    // Private variable that stores standard information
    Standard private standard;

    constructor(string memory _standard_name, string memory _standard_description) {

        standard.government = msg.sender;

        standard.standard_name = _standard_name;

        standard.description = _standard_description;
    }

}
