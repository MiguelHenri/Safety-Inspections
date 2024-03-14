# 🔎 Safety Inspections

This repository presents a framework for industrial safety inspections using a robot running ROS and blockchain.

# 🖋 Smart Contracts

This work presents six smart contracts (/codes) that regulate safety inspections. They are:

- `Regulations and Standards`: this contract is used by government entities to specify regulations and standards.
- `Request Inspection`: this contract is used by a requester to request an inspection in a specific place.
- `Robot Localization Data`: the robot uses this contract to share the data collected with the blockchain network.
- `Technical Specifications`: a manufacturing company uses this contract to share a component and its guidelines.
- `Maintenance`: technicians use this contract to share a component and data on its maintenance.
- `Inspection Results`: this contract receives the inspection results and the ROS bag IPFS CID.

For IPFS, see https://docs.ipfs.tech/.

# 🎮 Python Code and How to Run

This work presents Python scripts (/python) used to make transactions to an IBFT Hyperledger Besu blockchain network automatically. The time-evaluation Python script cleans ROS topic odometry data and transacts it to the blockchain network using the Web3.py library.

For Hyperledger Besu, see https://besu.hyperledger.org/23.4.0/private-networks/tutorials/ibft.
For Web3.py documentation, see https://web3py.readthedocs.io/en/stable/.

[to-do]
