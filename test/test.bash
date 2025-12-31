#!/bin/bash
set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
source /opt/ros/humble/setup.bash
colcon build

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || true

# ログを出力（デバッグ用）
cat /tmp/mypkg.log

# 成功判定
if grep -q '角の数10' /tmp/mypkg.log; then
  echo "🎉 Test Passed: found 角の数10"
  exit 0
else
  echo "❌ Test Failed: 角の数10 not found"
  exit 1
fi


