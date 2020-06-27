import RPi.GPIO as GPIO
import asyncio
from lila_api_call import isOnline

PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

# From: https://lichess.org/api#tag/Users
# "This API is very fast and cheap on lichess side. So you can call it quite
# "often (like once every 5 seconds)."

# 10 seconds is more than enough for my case but you can change it down to 5
SLEEP_TIME = 10

async def main():
    while True:
        if isOnline():
            GPIO.output(PIN, GPIO.HIGH)
        else:
            GPIO.output(PIN, GPIO.LOW)

        await asyncio.sleep(SLEEP_TIME)

if __name__ == '__main__':
    asyncio.run(main())
