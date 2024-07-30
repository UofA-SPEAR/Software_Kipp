#!/bin/bash

while true; do
  gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,clock-rate=90000,payload=96 ! \
  queue ! rtph264depay ! h264parse ! avdec_h264 ! \
  queue ! autovideoconvert ! fpsdisplaysink

  echo "Receiving pipeline exited. Restarting in 5 seconds..."
  sleep 5
done
