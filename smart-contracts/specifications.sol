// SPDX-License-Identifier: GPL-3.0 specifies the license for the Solidity code

// The pragma directive specifies the version of Solidity to be used for the contract
pragma solidity >=0.8.2 <0.9.0;

contract Specifications{

    struct Component{
        address manufacturer_address;
        string component_name;
        string guidelines;
        string fabrication_date;
    }

    Component public component;

    constructor(string memory _component_name, string memory _guidelines, string memory _fabrication_date) {

        component = Component(msg.sender, _component_name, _guidelines, _fabrication_date);
                
    }

    function getComponent() public view returns (Component memory) {
        return component;
    }

}
