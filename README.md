# 🔎 Safety Inspections

This repository presents a framework for industrial safety inspections using a robot running [ROS](https://docs.ros.org/) and blockchain.

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

This work presents Python scripts (/python) used to make transactions to an IBFT Hyperledger Besu blockchain network automatically. The time-evaluation Python script cleans ROS topic [odometry](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) data and transacts it to the blockchain network using the [Web3.py](https://web3py.readthedocs.io/en/stable/) library.

To run an IBFT Hyperledger Besu blockchain network, see :

- [How to run Besu.](https://besu.hyperledger.org/23.4.0/private-networks/tutorials/ibft)

To run transactions on the blockchain network, you must have the odometry (or other) ROS data in a file. The Python script first cleans the odom data, and then it sends the data, making transactions. Lastly, the transaction times will be saved in an out_times.txt file. This way, you may evaluate your blockchain network.

⚠️ Make sure:
- You have the python script downloaded;
- The input file is named correctly;
- The input file is being processed correctly;
- Your blockchain network is working fine;

# 📒 Charts

Used for research purposes. It calculates the hashing time for building a Merkle Tree.

# 🤝 Contributor

https://github.com/rodrigodg1
