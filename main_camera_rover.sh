gst-launch-1.0 -v zedsrc camera-sn=31826195 ! timeoverlay ! tee name=split has-chain=true ! \
 queue ! autovideoconvert ! fpsdisplaysink \
 split. ! queue max-size-time=0 max-size-bytes=0 max-size-buffers=0 ! autovideoconvert ! \
 nvh265enc bitrate=3000 ! h265parse ! rtph265pay config-interval=-1 pt=96 ! queue ! \
 udpsink host=192.168.1.2 port=5000 max-bitrate=3000000 sync=false async=false
