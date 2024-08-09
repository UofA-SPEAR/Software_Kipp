#!/bin/bash

# Replace with the actual serial number of your webcam
SERIAL_NUMBER="66255C60"

# Find the device path based on the serial number
DEVICE_PATH=$(sudo udevadm info --query=all --name=/dev/video* | grep 'ID_SERIAL_SHORT' | grep "$SERIAL_NUMBER" | awk -F= '{print $2}')

if [ -z "$DEVICE_PATH" ]; then
    echo "Error: Device with serial number $SERIAL_NUMBER not found."
    exit 1
fi

echo "Using device path: $DEVICE_PATH"

# Run gst-launch-1.0 with the found device path
gst-launch-1.0 v4l2src device=$DEVICE_PATH ! video/x-raw, format=GRAY8, width=340, height=340, framerate=30/1 ! videoconvert ! x264enc tune=zerolatency ! h264parse ! rtph264pay pt=127 config-interval=4 ! udpsink host=192.168.1.10 port=5000
