// SPDX-License-Identifier: GPL-3.0 specifies the license for the Solidity code

// The pragma directive specifies the version of Solidity to be used for the contract
pragma solidity >=0.8.2 <0.9.0;

// RequestContract is a smart contract
contract RequestContract {
    // Private variable that stores the place of inspection
    string private place;

    // Private variable that stores the address of the manager
    address private manager;

    // Request is a struct that represents a request for inspection
    struct Request {
        address requester;
        string date;
    }

    // Private array of inspection requests
    Request[] private requests;

    // Constructor function that initializes the contract with a list of valid locations and sets the manager's address to the creator of the contract
    constructor(string memory _place) {
        place = _place;
        manager = msg.sender;
    }

    // InpectionRequest function creates an inspection request and adds it to the requests array if the requested location is valid
    function InpectionRequest(string memory _date) public {
        require(msg.sender == manager, "only manager is allowed to request inspection"); // NEEDED??

        // Add a new Request to the requests array with the requester's address, date of inspection, and location of inspection
        requests.push(Request(msg.sender, _date));
    }

    // getPlace function returns the place of inspection
    function getPlace() public view returns (string memory) {
        return place;
    }

    // GetRequests function returns the list of inspection requests
    function getRequests() public view returns (Request[] memory) {
        return requests;
    }

}
