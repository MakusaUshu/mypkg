#!/bin/bash

set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
source /opt/ros/humble/setup.bash
colcon build


timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
 
grep '角の数10' /tmp/mypkg.log
