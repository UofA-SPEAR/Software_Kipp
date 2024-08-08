#!/bin/bash

while true; do
  gst-launch-1.0 v4l2src device=/dev/video4 ! video/x-raw,format=GRAY8,width=340,height=340,framerate=30/1 ! \
  tee name=t ! queue ! videoconvert ! autovideosink \
  t. ! queue ! videoconvert ! x264enc byte-stream=true tune=zerolatency speed-preset=ultrafast bitrate=3000 ! \
  h264parse ! rtph264pay config-interval=-1 pt=96 ! queue ! \
  udpsink host=192.168.1.10 port=5000 max-bitrate=3000000 sync=false async=false

  echo "Pipeline exited. Restarting in 5 seconds..."
  sleep 5
done


# gst-launch-1.0 v4l2src device=/dev/video4 ! videoconvert ! autovideosink
