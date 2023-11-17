#std_msg/Header
#https://docs.ros.org/en/melodic/api/std_msgs/html/msg/Header.html
#Fill seq, note the limit of uint 32
#Fill time stamp using epoch  

std_msgs/Header header   # Includes a timestamp
float32 throttle         # Throttle command, range 0-1
float32 steering         # Steering command, range -1 to 1
float32 turn             # Turn-in-place command, negative for left, positive for right