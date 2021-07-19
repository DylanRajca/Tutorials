from time import *
from threading import Thread

def myBox():
    while True:
        print('My Box is open')
        sleep(5)
        print('My box is closed')
        sleep(5)


def myLED(delayT):
    while True:
        print('My LED is on')
        sleep(delayT)
        print('my LED is off')
        sleep(delayT)


# declare variable that will be used as argument for Thread
delayLED = 1

# declare threads (if passing only one arg, must leave trailing comma)
boxThread = Thread(target=myBox)
LEDThread = Thread(target=myLED, args=(delayLED,))

# kill threads when program is stopped
boxThread.daemon = True
LEDThread.daemon = True

boxThread.start()
LEDThread.start()

# pause program to prevent it from ending, so our threads can run
while True:
    pass
