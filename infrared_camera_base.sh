# #!/bin/bash

# while true; do
#   gst-launch-1.0 udpsrc port=5010 ! application/x-rtp,clock-rate=90000,payload=96 ! \
#   queue ! rtph264depay ! h264parse ! tee name=t ! queue ! \
#   avdec_h264 ! videoconvert ! autovideosink \
#   t. ! queue ! matroskamux ! filesink location=output.mkv sync=false async=false

#   echo "Receiving pipeline exited. Restarting in 5 seconds..."
#   sleep 5
# done

# gst-launch-1.0 udpsrc port=5080 ! application/x-rtp, encoding-name=RAW ! rtpvrawdepay ! videoconvert ! autovideosink
gst-launch-1.0 udpsrc port=5080 ! application/x-rtp, payload=127 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
