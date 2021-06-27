import sys
import time
import RPi.GPIO as GPIO
import threading

CONTROL_SEQ = [[1, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1],[0, 1, 1, 0],[0, 0, 1, 0],[1, 1, 0, 0],[0, 1, 0, 0]]
REV_CONTROL_SEQ = CONTROL_SEQ[::-1]
CONTROL_DELAY = 0.001
TURN_STEPS = 260
TURN_SECS = 5.0
CHAN_LEFT = [17,27,22,23]
CHAN_RIGHT = [19,26,16,20]
     
def spin(chan_list, turns):

    arr = CONTROL_SEQ if turns >= 0.0 else REV_CONTROL_SEQ        
    steps = int(abs(turns) * TURN_STEPS)
    spin_delay = (TURN_SECS / steps) - CONTROL_DELAY * len(arr)
    
    for i in range(steps):
        time.sleep(spin_delay)
        for x in arr:        
            GPIO.output(chan_list, x)
            time.sleep(CONTROL_DELAY)
            
    GPIO.output(chan_list, (0,0,0,0))

def setup_motors():
    GPIO.setmode(GPIO.BCM)
    # Set all pins as output
    for pin in CHAN_LEFT + CHAN_RIGHT:
        GPIO.setup(pin, GPIO.OUT)
        
def cleanup():
    GPIO.output(CHAN_LEFT, (0,0,0,0))
    GPIO.output(CHAN_RIGHT, (0,0,0,0))
    
    sys.exit()
        
def command_motors(turnsl, turnsr):

    motorl = threading.Thread(target=spin, args=(CHAN_LEFT, turnsl))
    motorr = threading.Thread(target=spin, args=(CHAN_RIGHT, turnsr))

    motorl.start()
    motorr.start()
    #motorl.join()
    #motorr.join()


def test_two_steppers():
    setup_motors()
    #spin(CHAN_LEFT, 1)
    #spin(CHAN_RIGHT, 1)
    while True:
        try:
            turnsl, turnsr = input("Enter turnsl turnsr: ").split()
            print(turnsl)
            command_motors(float(turnsl), float(turnsr))
        except:
            cleanup()
        

if __name__ == '__main__':
    test_two_steppers()
