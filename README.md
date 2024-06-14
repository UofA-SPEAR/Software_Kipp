# Software_Kipp

## kipp_sensors
To publish gps coordinates, you can run either ```gps_node.py``` which uses data from the actual gps hardware, or ```Random_gps_node.py``` which generates random gps coordinates formatted in the traditional NavSatFix format.
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
