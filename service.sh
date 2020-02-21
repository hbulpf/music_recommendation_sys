#!/bin/bash

# 杀死进程
echo 'stop service...'
ps -ef | grep main.py | grep -v grep|cut -c 9-15|xargs kill -9
# 生成模型文件
python model.py
# 后台服务启动进程
if [ $?	== 0 ]
then
  echo 'start service...'
  nohup python main.py > music.log &
end