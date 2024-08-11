#!/bin/bash

# Start Node 1 in a new terminal
gnome-terminal -- bash -c "export ROS_DOMAIN_ID=10; source /home/prjadmin/Desktop/Software_Kipp/install/setup.bash; ros2 launch kipp_bringup base_enviromental_task.launch.py"

gnome-terminal -- bash -c "source /home/prjadmin/Desktop/kipp_circ_arm/install/setup.bash; ros2 run kipp_arm_encoder kipp_arm_calibrate"

gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/backup_camera_base.sh"

gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/main_camera_base.sh"

gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/arm_camera_base.sh"
