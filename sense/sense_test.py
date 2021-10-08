from pigpio_dht import DHT11
#Need to enable GPIO ports by using pigpio
#sudo pigpiod
gpio = 4 # BCM Numbering
sensor = DHT11(gpio)

def go():
   
    result = sensor.read()
    
    print('sensor reading: ', result)
    temp_far = result.get('temp_f')
    hum = result.get('humidity')
    val = result.get('valid')
    
    return_str = '\n'
    
    if result.get('valid') == True:   
        str_temp = "Temp Fahrenheit: " + str(temp_far) + '\n'
        str_hum = "Humidity: " + str(hum) 
        return_str += str_temp
        return_str += str_hum
    else:      
        return_str += 'Sensor reading failed'
    
    return return_str


go()
# uncomment call to troubleshoot standalone script
# keys: temp_f , humidity , valid
