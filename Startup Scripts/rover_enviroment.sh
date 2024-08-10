#!/bin/bash

# Start Node 1 in a new terminal
gnome-terminal -- bash -c "export ROS_DOMAIN_ID=10; source /home/spearua/Desktop/Software_Kipp/install/setup.bash; source /home/spearua/Desktop/kipp_circ_arm/install/setup.bash; ros2 launch kipp_bringup rover_enviromental_task.launch.py"

gnome-terminal -- bash -c "/home/spearua/Desktop/Software_Kipp/backup_camera_rover.sh"

gnome-terminal -- bash -c "/home/spearua/Desktop/Software_Kipp/main_camera_rover.sh"