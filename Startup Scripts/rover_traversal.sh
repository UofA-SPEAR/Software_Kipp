#!/bin/bash

# Name of the tmux session
SESSION_NAME="ros2_session"

# Start a new tmux session
tmux new-session -d -s $SESSION_NAME

# Start Node 1 in a new tmux window
tmux new-window -t $SESSION_NAME:1 -n "Node1"
tmux send-keys -t $SESSION_NAME:1 "export ROS_DOMAIN_ID=10; source /home/spearua/Desktop/Software_Kipp/install/setup.bash; source /home/spearua/Desktop/kipp_circ_arm/install/setup.bash; ros2 launch kipp_bringup rover_traversal.launch.py" C-m

# Start backup camera script in another new tmux window
tmux new-window -t $SESSION_NAME:2 -n "BackupCamera"
tmux send-keys -t $SESSION_NAME:2 "/home/spearua/Desktop/Software_Kipp/backup_camera_rover.sh" C-m

# Start main camera script in another new tmux window
tmux new-window -t $SESSION_NAME:3 -n "MainCamera"
tmux send-keys -t $SESSION_NAME:3 "/home/spearua/Desktop/Software_Kipp/main_camera_rover.sh" C-m

# #Arm Camera
# tmux new-window -t $SESSION_NAME:4 -n "ArmCamera"
# tmux send-keys -t $SESSION_NAME:4 "/home/spearua/Desktop/Software_Kipp/arm_camera_rover.sh" C-m

#Infrared Camera
tmux new-window -t $SESSION_NAME:5 -n "Infrared Camera"
tmux send-keys -t $SESSION_NAME:5 "/home/spearua/Desktop/Software_Kipp/infrared_camera_rover.sh" C-m

#Aruco Camera
tmux new-window -t $SESSION_NAME:6 -n "ArucoCamera"
tmux send-keys -t $SESSION_NAME:6 "source /home/spearua/Desktop/Software_Kipp/install/setup.bash; source /home/spearua/Desktop/kipp_circ_arm/install/setup.bash; ros2 run kipp_camera aruco_node" C-m

# # Optional: Attach to the tmux session to view the windows
tmux attach-session -t $SESSION_NAME
