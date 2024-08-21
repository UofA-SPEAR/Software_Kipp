#!/bin/bash

# Use the symlink for the infrared camera
DEVICE_PATH="/dev/v4l/by-id/usb-046d_Logitech_BRIO_734C0A89-video-index2"

# Alternatively, you can use the by-path symlink
# DEVICE_PATH="/dev/v4l/by-path/platform-3610000.usb-usb-0:3.3:1.0-video-index2"

echo "Using infrared camera at: $DEVICE_PATH"

# Run gst-launch-1.0 with the infrared camera device path
gst-launch-1.0 v4l2src device=$DEVICE_PATH ! video/x-raw, format=GRAY8, width=340, height=340, framerate=30/1 ! videoconvert ! x264enc tune=zerolatency ! h264parse ! rtph264pay pt=127 config-interval=4 ! udpsink host=192.168.1.10 port=5080
# gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-raw, format=GRAY8, width=340, height=340, framerate=30/1 ! videoconvert ! x264enc tune=zerolatency ! h264parse ! rtph264pay pt=127 config-interval=4 ! udpsink host=192.168.1.10 port=5080


