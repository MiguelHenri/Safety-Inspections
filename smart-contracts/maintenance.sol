// SPDX-License-Identifier: GPL-3.0 specifies the license for the Solidity code

// The pragma directive specifies the version of Solidity to be used for the contract
pragma solidity >=0.8.2 <0.9.0;

// This contract details a maintenance made by a technician in any component
contract Maintenance{

    struct Component{
        address technician_address;
        string component_name;
        string description;
    }

    Component public component;

    constructor(string memory _component_name, string memory _description) {

        component = Component(msg.sender, _component_name, _description);
                
    }

    function getComponent() public view returns (Component memory) {
        return component;
    }

}
