#Pi3 IoT project by using MySQL & PHP


This is project that uses a DHT11 sensor to track tempature and humidity indoors. And it can store temperature data into a specific database by a interval time. 

STEPS:

1. Create DHT11.py

2. Create iot_temp_url_git.py

3. Create settemp.php and showtemp.php and put them in /var/www/ or /var/www/html/

4. Create gettemp.sh

5. The last step is that: 
   $sudo nano ~/.config/lxsession/LXDE-pi/autostart
   Then add a row of script: @sh /home/pi/pi3iotgit/gettemp.sh (refer to ../raspberry/tutorial/shell/ )

6. You can have a try and add data to your database:
   Open chrome and key url"X.x.x.x/settemp.php?id=1&temp=22",you would see your database add one record of temperature. Check it out by key url"x.x.x.x/showtemp.php" and press refresh button.

7. Check it out to see if the content of database get refreshed by a interval time via the program of "iot_temp_url_git.py"

REFERENCES:

1.https://github.com/adafruit/Adafruit_Python_DHT


