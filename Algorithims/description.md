#  Algorithims

These are various algorithims in work that either:
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
