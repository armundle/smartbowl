# Reads data from the sensor and sends a text if new food is detected.

import time
import callServer

POLL_FREQ_IN_S = 5
MIN_TIME_THRESHOLD = 1
WEIGHT_THRESHOLD_IN_G = 100
FEEDING_FREQ = 12


# replace with getData module
def getData():
    return 0


# replace with sendText module
def notify():
    callServer.BoomerIsFed()


def run(debug=False):
    # Get data from the sensor
    data = getData()
    thresholdTime = 0

    while(True):
        time.sleep(POLL_FREQ_IN_S)
        if (data > WEIGHT_THRESHOLD_IN_G):
            thresholdTime += 1
            if(thresholdTime > MIN_TIME_THRESHOLD):
                notify()
                thresholdTime = 0
        else:
            if debug:
                print "continue"
            continue

run(True)
