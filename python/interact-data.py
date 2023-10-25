from web3 import Web3
from eth_account import Account
from solcx import compile_source
from web3.middleware import construct_sign_and_send_raw_middleware
from web3.middleware import geth_poa_middleware

def compile_sol():
    # Share data solidity source code
    compiled_sol = compile_source(
        '''
        // SPDX-License-Identifier: GPL-3.0

        pragma solidity >=0.8.2 <0.9.0;

        contract RobotLocalizationData {

            // Private variable that stores the place of inspection
            string private place;
            // Private variable that stores the date of inspection
            string private date;
            // Private variable that stores an array of inspector adresses
            address[] private inspectors;

            constructor() {
                place = "aqui";
                date = "outubro";
            }

            struct Time {
                uint32 secs;
                uint32 nsecs;
            }

            struct Vector3 {
                uint32 x;
                uint32 y;
                uint32 z;
            }

            struct Quaternion {
                uint32 x;
                uint32 y;
                uint32 z;
                uint32 w;
            }

            struct Pose {
                Vector3 position;
                Quaternion orientation;
            }

            struct Twist {
                Vector3 linear;
                Vector3 angular;
            }

            struct Header {
                uint32 seq;
                Time stamp;
                string frame_id;
            }

            struct PoseWithCovariance {
                Pose pose;
                uint32[36] covariance;
            }

            struct TwistWithCovariance {
                Twist twist;
                uint32[36] covariance;
            }

            struct Orientation {
                Quaternion o;
                uint[9] covariance;
            }

            struct Group {
                Vector3 a;
                uint[9] covariance;
            }

            struct Odom {
                Header header;
                string child_frame_id;
                PoseWithCovariance pose;
                TwistWithCovariance twist;
            }

            struct ImuAngular {
                Header header; 
                Vector3 vector;
            }

            struct ImuMag {
                Header header;
                Vector3 vector;
            }

            struct ImuData {
                Header header;
                Orientation orientation;
                Group angular_velocity;
                Group linear_acceleration;
            }

            // Public variables that stores robot data
            Odom public odom;
            ImuAngular public imu_angular;
            ImuMag public imu_mag;
            ImuData public imu_data;

            function updateOdom(
                uint32 seq,
                uint32 stampSecs,
                uint32 stampNsecs,
                string memory frameId,
                string memory childFrameId,
                uint32[3] memory position,
                uint32[4] memory orientation,
                uint32[36] memory poseCovariance,
                uint32[3] memory linear,
                uint32[3] memory angular,
                uint32[36] memory twistCovariance
            ) public {
                odom.header.seq = seq;
                odom.header.stamp.secs = stampSecs;
                odom.header.stamp.nsecs = stampNsecs;
                odom.header.frame_id = frameId;

                odom.child_frame_id = childFrameId;

                odom.pose.pose.position.x = position[0];
                odom.pose.pose.position.y = position[1];
                odom.pose.pose.position.z = position[2];

                odom.pose.pose.orientation.x = orientation[0];
                odom.pose.pose.orientation.y = orientation[1];
                odom.pose.pose.orientation.z = orientation[2];
                odom.pose.pose.orientation.w = orientation[3];

                for (uint256 i = 0; i < 36; i++) {
                    odom.pose.covariance[i] = poseCovariance[i];
                }

                odom.twist.twist.linear.x = linear[0];
                odom.twist.twist.linear.y = linear[1];
                odom.twist.twist.linear.z = linear[2];

                odom.twist.twist.angular.x = angular[0];
                odom.twist.twist.angular.y = angular[1];
                odom.twist.twist.angular.z = angular[2];

                for (uint256 i = 0; i < 36; i++) {
                    odom.twist.covariance[i] = twistCovariance[i];
                }
            }

            function updateImuMag(
                uint32 seq,
                uint32 stampSecs,
                uint32 stampNsecs,
                string memory frameId,
                uint32[3] memory position
            ) public {
                imu_mag.header.seq = seq;
                imu_mag.header.stamp.secs = stampSecs;
                imu_mag.header.stamp.nsecs = stampNsecs;
                imu_mag.header.frame_id = frameId;

                imu_mag.vector.x = position[0];
                imu_mag.vector.y = position[1];
                imu_mag.vector.z = position[2];
            }

            function updateImuAngular(
                uint32 seq,
                uint32 stampSecs,
                uint32 stampNsecs,
                string memory frameId,
                uint32[3] memory position
            ) public {
                imu_angular.header.seq = seq;
                imu_angular.header.stamp.secs = stampSecs;
                imu_angular.header.stamp.nsecs = stampNsecs;
                imu_angular.header.frame_id = frameId;

                imu_angular.vector.x = position[0];
                imu_angular.vector.y = position[1];
                imu_angular.vector.z = position[2];
            }

            function updateImuData(
                uint32 seq,
                uint32 stampSecs,
                uint32 stampNsecs,
                string memory frameId,
                uint32[4] memory orientation,
                uint32[9] memory o_covariance,
                uint32[3] memory angular_velocity,
                uint32[9] memory av_covariance,
                uint32[3] memory linear_acceleration,
                uint32[9] memory la_covariance
            ) public {
                imu_data.header.seq = seq;
                imu_data.header.stamp.secs = stampSecs;
                imu_data.header.stamp.nsecs = stampNsecs;
                imu_data.header.frame_id = frameId;

                imu_data.orientation.o.x = orientation[0];
                imu_data.orientation.o.y = orientation[1];
                imu_data.orientation.o.z = orientation[2];
                imu_data.orientation.o.w = orientation[3];
                
                for(uint i = 0; i < 9; i++){
                    imu_data.orientation.covariance[i] = o_covariance[i];
                }

                imu_data.angular_velocity.a.x = angular_velocity[0];
                imu_data.angular_velocity.a.y = angular_velocity[0];
                imu_data.angular_velocity.a.z = angular_velocity[2];

                for(uint i = 0; i < 9; i++){
                    imu_data.angular_velocity.covariance[i] = av_covariance[i];
                }

                imu_data.linear_acceleration.a.x = linear_acceleration[0];
                imu_data.linear_acceleration.a.y = linear_acceleration[0];
                imu_data.linear_acceleration.a.z = linear_acceleration[2];

                for(uint i = 0; i < 9; i++){
                    imu_data.linear_acceleration.covariance[i] = la_covariance[i];
                }
            }
        }
        ''',
        output_values=['abi', 'bin']
    )
    return compiled_sol

def interact(w3, compiled_sol):
    # Retrieve the contract interface
    contract_id, contract_interface = compiled_sol.popitem()

    # Getting contract bytecode (bin)
    bytecode = contract_interface['bin']

    # Getting contract abi
    abi = contract_interface['abi']

    # Private Key
    privateKey = '8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63'

    account = Account.from_key(privateKey)

    fromAddress = account.address

    nonce = w3.eth.get_transaction_count(fromAddress)

    # Contract Address
    contractAddress = '0xe135783649BfA7c9c4c6F8E528C7f56166efC8a6'

    # contract = w3.eth.contract(abi=abi, address=contractAddress, bytecode=bytecode)

    rawtxOptions = {
        'to': contractAddress,  
        'value': 0,
        'gas': 2000000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
        'data': bytecode,  
        'chainId': 1337
    }

    # Interacting with contract function
    signed_txn = w3.eth.account.sign_transaction(rawtxOptions, privateKey)

    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(receipt)


def main():
    # Compiling solidity contract
    compiled_sol = compile_sol()

    # Web3.py instance
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # print('Connected to Besu: ', w3.is_connected())

    interact(w3, compiled_sol)

if __name__ == "__main__":
    main()