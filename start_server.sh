#!/bin/bash
set -ex

IP_ADDRESS=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

# raspivid -o - -t 0 -w 640 -h 480 -fps 15 -b 200000 \
# raspivid -o - -t 0 -w 640 -h 480 -fps 15 \
#   | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264 &
#pid=$?
#while true
#do
#  vcgencmd measure_temp
#  sleep 0.5
#done
# | ffmpeg -y -i pipe:0 -c copy -f flv rtmp://localhost:8554/stream
#| ffmpeg -y -f h264 -i - -c:v copy -map 0:0 -f flv rtmp://192.168.1.151:8554/stream
/home/pi/.local/bin/uvicorn serve:app --host ${IP_ADDRESS} --log-level 'warning'

#kill $pid

