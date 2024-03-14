# 🔎 Safety Inspections

This repository presents a framework for industrial safety inspections using a robot running ROS and blockchain.

# 🤝 Contributor

https://github.com/rodrigodg1

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

To run transactions on the blockchain network, you may have the odometry (or other) ROS data in a file. Renaming the file in line 444 if needed (odom.txt) and running time-evaluation.py will make the transactions with the data collected automatically, one by one. The Python script first cleans the odom data, and then they send the data, making transactions. Lastly, the transaction times will be saved in an out_times.txt file. This way, you may evaluate your blockchain network.

# 📒 Charts

Used for research purposes. Calculates ROS data sizes, for example.
