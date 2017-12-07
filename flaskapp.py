import pyduino
import time
import atexit
from flask import Flask, request, redirect, url_for, send_from_directory

app = Flask(__name__, static_url_path='')


@app.before_first_request
def setupSerial():
    global arduino
    arduino = pyduino.Arduino(57600, '*', 0)




@app.route("/")
def page():
    if arduino.getConnStatus() == True:
        return app.send_static_file('index.html')


time.sleep(3)

# declare the pins we're using
LED_PIN = 5
ANALOG_PIN = 0


@app.before_first_request
def setupSerial():
	global arduino
	arduino=pyduino.Arduino(57600,'*',0)
# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def hello_world():

    # variables for template page (templates/index.html)
    author = "Kyle"

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'Turn On':
            print 'TURN ON'

            # turn on LED on arduino
            arduino.digital_write(LED_PIN,1)

        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off':
            print 'TURN OFF'

            # turn off LED on arduino
            arduino.digital_write(LED_PIN,0)

        else:
            pass

@atexit.register
def disconnect():
    if arduino.getConnStatus() == True:
        arduino.closePort()
        print('Port closed !!!')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')


