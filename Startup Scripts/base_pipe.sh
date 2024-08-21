#!/bin/bash

# # Start Node 1 in a new terminal
# gnome-terminal -- bash -c "export ROS_DOMAIN_ID=10; source /home/prjadmin/Desktop/Software_Kipp/install/setup.bash; ros2 launch kipp_bringup base_traversal.launch.py"

# gnome-terminal -- bash -c "source /home/prjadmin/Desktop/Software_Kipp/install/setup.bash; ros2 run kipp_navigation gps_map_node"

# gnome-terminal -- bash -c "source /home/prjadmin/Desktop/Software_Kipp/install/setup.bash; ros2 topic echo /aruco_marker_ids"

# gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/backup_camera_base.sh" # ZED M

# gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/main_camera_base.sh"

# gnome-terminal -- bash -c "/home/prjadmin/Desktop/Software_Kipp/infrared_camera_base.sh"



#!/bin/bash

# Name of the tmux session
SESSION_NAME="ros2_base_session"

# Start a new tmux session
tmux new-session -d -s $SESSION_NAME

# Start Node 1 in a new tmux window
tmux new-window -t $SESSION_NAME:1 -n "ROS_NODES"
tmux send-keys -t $SESSION_NAME:1 "export ROS_DOMAIN_ID=10; source /home/prjadmin/Desktop/Software_Kipp/install/setup.bash; ros2 launch kipp_bringup base_pipe.launch.py" C-m


# Start main camera script in another new tmux window
tmux new-window -t $SESSION_NAME:2 -n "BACKUP_CAMERA"
tmux send-keys -t $SESSION_NAME:2 "/home/prjadmin/Desktop/Software_Kipp/backup_camera_base.sh" C-m


#Infrared Camera
tmux new-window -t $SESSION_NAME:3 -n "Main Camera"
tmux send-keys -t $SESSION_NAME:3 "/home/prjadmin/Desktop/Software_Kipp/main_camera_base.sh" C-m

tmux new-window -t $SESSION_NAME:4 -n "Infared Camera"
tmux send-keys -t $SESSION_NAME:4 "/home/prjadmin/Desktop/Software_Kipp/infrared_camera_base.sh" C-m

# # Optional: Attach to the tmux session to view the windows
tmux attach-session -t $SESSION_NAME
