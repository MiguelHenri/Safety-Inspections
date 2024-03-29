// SPDX-License-Identifier: GPL-3.0 specifies the license for the Solidity code

// The pragma directive specifies the version of Solidity to be used for the contract
pragma solidity >=0.8.2 <0.9.0;

// ResultsContract is a smart contract that stores the results of inspections
contract ResultsContract {
    // Private variable that stores the place of inspection
    string private place;

    // Private variable that stores the address of the manager
    address private manager;

    // Result is a struct that represents the results of an inspection
    struct Result {
        address inspector;
        string result;
        string IPFS_rosbag_cid;
    }

    // Public array of inspection results
    Result[] public results;

    // Constructor function that initializes the contract with a list of valid locations and sets the manager's address to the creator of the contract
    constructor(string memory _place) {
        place = _place;
        manager = msg.sender;
    }

    // InspectionResult function creates an inspection result and adds it to the results array
    function InspectionResult(
        string memory _result,
        string memory _IPFS_rosbag_cid
    ) public {
        // Add a new Result to the results array with the inspector's address, location of inspection, and the result of the inspection
        results.push(
            Result(msg.sender, _result, _IPFS_rosbag_cid)
        );
    }

    // GetResults function returns the array of results
    function getResults() public view returns (Result[] memory) {
        return results;
    }
}

