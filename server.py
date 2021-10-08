from flask import Flask, render_template
from flask_apscheduler import APScheduler
# Flask is the python server
from logger import logger
# logger is the module that I created to write to a text file (log.txt)
from sense import sense
# sense is the module that I created to get a sensor reading from my DHT11 Temp/Humidity Sensor
#Need to enable GPIO ports by using pigpio
#sudo pigpiod
from pigpio_dht import DHT11 # need to initialize the DHT11 here
#if initialize in sense module then mulitple instances will be created
#too many instances is a problem


class Config:
    SCHEDULER_API_ENABLED = True
    
# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
app.config.from_object(Config())


# initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

#initialize DHT11 sensor
gpio = 4 # BCM Numbering
sensor = DHT11(gpio)


#scheduled task 
@scheduler.task('interval', id='do_job_1', seconds=600, misfire_grace_time=900)
def job1():
    data = sense.go(sensor)
    logger.log(data)


#Routes 

@app.route("/")
@app.route("/index")
def index():
    name = 'Justin'
    return render_template('index.html', title='Welcome', username=name)


@app.route('/logdata')
def logdata():
    data = logger.read()
    #data is an array
    #need to test edge cases 
    return render_template('data.html', title='Data Log', members=data)


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()



