from threading import Thread
import RPi.GPIO as GPIO
import time

#GPIO 17
keys = {
        'L1': 11,
        'L2': 12
    }

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def detectKey(key, value):
    GPIO.setup(value, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        if(GPIO.input(value)==1):
            print(f"{key} Button pressed")
            time.sleep(0.5)


for k, v in keys.items():
    x = Thread(target=detectKey, args=(k,), kwargs={'value':v}, name=f"{k}-button-detect", daemon=True)
    x.start()


while True:
    pass
