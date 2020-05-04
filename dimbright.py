#!/usr/bin/env python3
#coding:utf-8
import os
import subprocess
with open ('/usr/dimbright.sh', 'w') as sf:
    sf.write('#!/bin/bash'+'\n')
    sf.write('SHELL=/bin/sh PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin'+'\n')
    sf.write('echo $1 > /sys/class/backlight/intel_backlight/brightness'+'\n')
os.chmod('/usr/dimbright.sh', 0o755)    
with open ('/etc/udev/rules.d/dimbright.rules', 'w') as rf:
    rf.write('SUBSYSTEM=="power_supply", ENV{POWER_SUPPLY_ONLINE}=="1", RUN+="/usr/dimbright.sh 7125"'+'\n')    
    rf.write('SUBSYSTEM=="power_supply", ENV{POWER_SUPPLY_ONLINE}=="0", RUN+="/usr/dimbright.sh 3750"'+'\n')

l = subprocess.call(['udevadm', 'control', '-R'])
