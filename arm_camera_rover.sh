#!/bin/bash

# Replace with your specific serial number
SERIAL_NUMBER="66255C60"

# Find the primary video device path using the serial number (typically video-index0)
DEVICE_PATH=$(find /dev/v4l/by-id/ -name "*$SERIAL_NUMBER-video-index0")

# Check if the device path was found
if [ -z "$DEVICE_PATH" ]; then
    echo "No device found with serial number: $SERIAL_NUMBER"
    exit 1
fi

# Use the device path in the GStreamer pipeline to stream over UDP on port 5100
echo "Using camera at: $DEVICE_PATH"
gst-launch-1.0 v4l2src device="$DEVICE_PATH" ! videoconvert ! x264enc tune=zerolatency ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.1.10  port=5040

