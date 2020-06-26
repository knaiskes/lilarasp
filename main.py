import RPi.GPIO as GPIO
from lila_api_call import isOnline

PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)
GPIO.setup(PIN, GPIO.OUT)

def main():
    print(isOnline())


if __name__ == '__main__':
    main()
