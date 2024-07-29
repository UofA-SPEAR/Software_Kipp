gst-launch-1.0 -v udpsrc port=5000 caps="application/x-rtp, media=video, encoding-name=H265, payload=96" ! \
 rtph265depay ! h265parse ! avdec_h265 ! tee name=t ! queue ! autovideosink t. ! queue ! \
 autovideoconvert ! tcpserversink host=0.0.0.0 port=7000
