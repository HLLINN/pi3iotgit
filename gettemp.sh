#!/bin/bash
#program:
#      This program is for automatic opening DHT11 and breathing lights while turn on PI3.
#History:
# 22/December/2018   R.L. First release
# 1/January/2018     R.L. revised : add iot_temp_url.py instead of test_DHT11.py or Ch11_3_3.py
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
sudo python /home/pi/pi3iot/iot_temp_url.py &
sudo python /home/pi/personal/breathing_lights.py
