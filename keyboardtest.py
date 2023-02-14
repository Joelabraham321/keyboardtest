#Pynput is a library that takes command from a Keyboard
from pynput import keyboard
#Import Jetson.GPIO allows access to the Jetson Boards GPIO Pins
import Jetson.GPIO as GPIO 
#Import Time Listens and adds delays as needed
import time 

#Roboclaw import command
from roboclaw_3 import Roboclaw

   

#Global pins Defined from GPIO Pins to classfied letters
# W_Command = 7
# A_Command = 11
# S_Command = xx
# D_Command = xx


# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD)
# GPIO.setup(W_Command, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(A_Command, GPIO.OUT, initial=GPIO.LOW)
# wGPIO.setup(S_Command, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(D_Command, GPIO.OUT, initial=GPIO.LOW)

if __name__ == "__main__":w
   
    address = 0x80
    roboclaw = Roboclaw("/dev/ttyTHS1", 115200)
    roboclaw.Open()

def on_press(key):
    try:
        if key.char == 'w':
            roboclaw.SpeedAccelM1M2(address,0,1000,1000)
            #roboclaw.SpeedM2(address,1000)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key.char == 'w':
        roboclaw.SpeedAccelM1M2(address,0,0,0)
        #roboclaw.SpeedM2(address,0)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listener.start()