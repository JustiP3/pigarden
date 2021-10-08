Goals:

Get sensor values an write to text periodically
This will be the internal server for each rasberry pi 
Each internal server needs to be able to send data to the main server
(yet to be created)

Note:
This is a python3 server. Use python3 command to run the server.
Need to enable GPIO ports by using pigpio
sudo pigpiod
pigpio reference (http://abyz.me.uk/rpi/pigpio/python.html)


Current Status:

-can write to file with variable data
-periodic tasks are working
-Wired DHT11 sensor
-Can get input from sensor HOWEVER,
-Sometimes the sensor fails (this is normal, apparently)
-Sensor fails A LOT, how much failure is normal?
-everything is working, can sense and write to text file
-overnight test passed - sensor can continuously read for at least 24 hrs



Next Steps:
how much sensor failure is normal for DHT11? research / troubleshoot

how to execute a program on startup
** need to enable pipgio on startup and start the server **

wire up and test other devices
-lcd screen
-digital temp
-button
-rotary encoder 
-relay

How will this be powered? (question to be answered later)
How to incoperate solar power (later)



Error Codes:

1. Did not enable pigpio 
	Can't connect to pigpio at localhost(8888)

	Did you start the pigpio daemon? E.g. sudo pigpiod

	Did you specify the correct Pi host/port in the environment
	variables PIGPIO_ADDR/PIGPIO_PORT?
	E.g. export PIGPIO_ADDR=soft, export PIGPIO_PORT=8888

	Did you specify the correct Pi host/port in the
	pigpio.pi() function? E.g. pigpio.pi('soft', 8888)
Soultion:
Enable pigpio. in terminal type command:
sudo pigpiod

2. Device is not connected on specified gpio pin
	Traceback (most recent call last):
	  File "sense.py", line 11, in <module>
		go()
	  File "sense.py", line 7, in go
		result = sensor.read()
	  File "/home/pi/.local/lib/python3.7/site-packages/pigpio_dht/dhtxx.py", line 74, in read
		result = self._read()
	  File "/home/pi/.local/lib/python3.7/site-packages/pigpio_dht/dhtxx.py", line 256, in _read
		raise TimeoutError("{} sensor on GPIO {} has not responded in {} seconds. Check sensor connection.".format(self.__class__.__name__, self.gpio, self.timeout_secs))
	TimeoutError: DHT11 sensor on GPIO 2 has not responded in 0.5 seconds. Check sensor connection.
Solution:
Is device broken?
Check connections
Check specified GPIO pin is correct. 

3. Too many pgpio instances 
Error Message:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Can't connect to pigpio at localhost(8888)

Can't create callback thread.
Perhaps too many simultaneous pigpio connections.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
What is happening?
You are setting up device inside the while loop, so it creates multiple instances 
of same device, hence the error code

Can't create callback thread.
Perhaps too many simultaneous pigpio connections.
You need to create one device instance and read the info from sensor chronically. 

Solution:
initialize sensor in server and pass that sensor to the sense module. 
Initially, the server would periodically call the 'sense' module.
The sense module instantiated a new instance every time. 


Interesting Failures along the way
-I didn't know the name of the temp / humidity sensor that I was working with
-I thought I needed to communicate via I2C
-That Turned out to not be true.
- I was able to access strange data from the sensor using i2c
-could read values continuously with test code

