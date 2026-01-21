#!/bin/bash
set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash

timeout 6 bash -c "
ros2 run mypkg talker &
ros2 run mypkg listener
" > /tmp/mypkg.log 2>&1 || true

cat /tmp/mypkg.log

if grep -q '角の数' /tmp/mypkg.log; then
  echo "🎉 Test Passed"
  exit 0
else
  echo "❌ Test Failed"
  exit 1
fi
