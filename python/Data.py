import yaml

# Odom Data structure
class Data:
	seq: int = -1
	secs: int = -1
	nsecs: int = -1
	frame_id: str = ""
	child_frame_id: str = ""
	position_x: int = -1
	position_y: int = -1
	position_z: int = -1
	orientation_x: int = -1
	orientation_y: int = -1
	orientation_z: int = -1
	orientation_w: int = -1
	covariance: list = []
	linear_x: int = -1
	linear_y: int = -1
	linear_z: int = -1
	angular_x: int = -1
	angular_y: int = -1
	angular_z: int = -1
	twist_covariance: list = []

# Function used to read the odom.txt file
def read_file(file_name):
	with open(file_name, 'r') as file:
		data = file.read()
	return data

# Function used to convert txt data into Data structure
def clear(block):
	
	clean = Data()
	data = yaml.safe_load(block)
    
	clean.seq = int(data['header']['seq'])
	clean.secs = int(data['header']['stamp']['secs'])
	clean.nsecs = int(data['header']['stamp']['nsecs'])
	clean.frame_id = data['header']['frame_id']
	clean.child_frame_id = data['child_frame_id']
	clean.position_x = int(data['pose']['pose']['position']['x'])
	clean.position_y = int(data['pose']['pose']['position']['y'])
	clean.position_z = int(data['pose']['pose']['position']['z'])
	clean.orientation_x = int(data['pose']['pose']['orientation']['x'])
	clean.orientation_y = int(data['pose']['pose']['orientation']['y'])
	clean.orientation_z = int(data['pose']['pose']['orientation']['z'])
	clean.orientation_w = int(data['pose']['pose']['orientation']['w'])
	clean.covariance = data['pose']['covariance']
	clean.covariance = [int(i) for i in clean.covariance]
	clean.linear_x = int(data['twist']['twist']['linear']['x'])
	clean.linear_y = int(data['twist']['twist']['linear']['y'])
	clean.linear_z = int(data['twist']['twist']['linear']['z'])
	clean.angular_x = int(data['twist']['twist']['angular']['x'])
	clean.angular_y = int(data['twist']['twist']['angular']['y'])
	clean.angular_z = int(data['twist']['twist']['angular']['z'])
	clean.twist_covariance = data['twist']['covariance']
	clean.twist_covariance = [int(i) for i in clean.twist_covariance]
		
	return clean

# Function used to 'clean' all file data
def clean_odom(file_name):

	# reads imu_data.txt file
	data = read_file(file_name)

	# cleans header
	blocks = data.strip().split('---')

	# converts block txt data to Data structure
	clean_blocks = []
	for block in blocks:
		if block:
			clean_blocks.append(clear(block))
			
	return clean_blocks

# Debugging clean_odom
def print_odom(odom_data):
    for odom in odom_data:
            print('--This--')
            print(odom.seq)
            print(odom.secs)
            print(odom.nsecs)
            print(odom.frame_id)
            print(odom.child_frame_id)
            print([odom.position_x,
                odom.position_y,
                odom.position_z])
            print([odom.orientation_x,
                odom.orientation_y,
                odom.orientation_z,
                odom.orientation_w])
            print(odom.covariance)
            print([odom.linear_x,
                odom.linear_y,
                odom.linear_z])
            print([odom.angular_x,
                odom.angular_y,
                odom.angular_z])
            print(odom.twist_covariance)