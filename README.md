# Software_Kipp

## kipp_sensors
To publish gps coordinates, you can run either ```gps_node.py``` which uses data from the actual gps hardware, or ```random_gps_node.py``` which generates random gps coordinates formatted in the traditional NavSatFix format.
To run either:
```ros2 run kipp_sensors gps_node``` or
```ros2 run kipp_sensors random_gps_node```

Then there is another node ```save_gps_node.py``` that saves the gps coordinates to a file ```gps_coordinates.txt``` every 2 seconds when this boolean trigger is ran: ```ros2 service call /trigger_action std_srvs/srv/SetBool "{data: true}"```

Or the opposite ```ros2 service call /trigger_action std_srvs/srv/SetBool "{data: false}"```

## kipp_file_transfer
to send a file:

```ros2 run kipp_file_transfer file_send --ros-args -p file_path:=/path/to/file -p server_ip:=IPADRESS -p port:=PORT#```

to recieve a file:

```ros2 run kipp_file_transfer file_receive --ros-args -p server_ip:=IPADRESS -p port:=PORT# -p output_file:=name_of_file.txt```

#  Algorithms

These are various algorithms in work that either:
    - need to be intergrated into a ros2 node
    OR:
    - need to be interfaced with GUI, running on the base station

## Current  Code

### ArUco.py
This detects the Aruco marker and displays results on the screen. This needs to be intergrated with GUI. We are using 4X4_100 for CIRC.

### Blue_color_trace.py
This code is responsible for detecting blue light and figuring out where the average of the light is on the z axis, allowing us to add additional code to determine whether the rover needs to move left, right or straight. This would be a node

### Red_color_trace.py
This code is responsible for detecting red light and figuring out where the average of the light is on the z axis, allowing us to add additional code to determine whether the rover needs to move left, right or straight. This would be a node

### Panorama.py
Needs to be converted to a node. Is given a directory to index for all image files and stitches them together

### Photographer.py
This code wont actually be used, but its a siple script that takes photos by clicking the space bar which makes testing/debuging algorithis a lot easier.
