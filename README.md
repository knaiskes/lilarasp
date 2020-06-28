# lilarasp

lilarasp is a Python script running on a Raspberry Pi which checks if a
[lichess.org](https://lichess.org/) user is online. While the user is online
the led will be on.

# Motivation

The motivation behind this script is that the current World Chess Champion
([Magnus Carlsen](https://en.wikipedia.org/wiki/Magnus_Carlsen)) regularly
plays chess on [lichess.org](https://lichess.org/) and I keep missing watching
his games live. I hope from now and on I won't!

### Requirements

- Python >= 3.7
- Raspberry Pi (any version)
- 1 breadboard (optional but useful)
- 2 male to female jumper wires
- 1 led
- 1 resistor ([can be anything over about 50Ω](https://projects.raspberrypi.org/en/projects/physical-computing/2))

### Wiring circuit

[Turning on an LED with your Raspberry Pi's GPIO Pins](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)


### Setup

Clone repo
```
$ git clone git@github.com:KNaiskes/lilarasp.git
```

Open with you editor the file lila_api_call.py and add to variable USERNAME the
lichess.org username you are intrested in
```
URL = 'https://lichess.org/api/user/'
USERNAME = ''
```

Run script
```
$ cd lilarasp/
$ sudo python3 main.py
```
[![Project Videp](https://user-images.githubusercontent.com/6069054/85946632-5aca0c80-b94e-11ea-8b0b-5c872698a49e.png)](https://www.youtube.com/watch?v=OKR5sdUfYUw)
