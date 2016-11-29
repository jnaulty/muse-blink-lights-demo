# Muse Blink Light Demo

This code was written to demo how easy it is to integrate a mobile, consumer-grade EEG device with an Arduino microcontroller.

This demo requires basic skills in hardware and intermediate skills in software development, you should be able to run a python3 script on your computer, and load an arduino script to an Arduino microcontroller.

An outline of the project flow:
-   upload script to arduino
-   connect muse to computer (bluetooth)
-   run muse-io 
-   run blink.py script

## Prep Work


-   Install [Muse SDK](http://developer.choosemuse.com/research-tools/getting-started)
-   Install [Arduino IDE](https://www.arduino.cc/en/Main/Software)
-   Requres Python 3
    -   python3 -m venv venv-muse
    -   source venv-muse/bin/activate
    -   pip install -r requirements.txt


## Starting

### Arduino

-   Load the `led_blink.ino` onto your Arduino
-   record Arduino port name e.g. `/dev/ttyACM0`

### Muse

-   connect muse device to bluetooth
-   run muse-io to get started.
-   For linux users, this is done by running: `./muse-io --device <mac-address> --osc osc.udp://localhost:5000`
    -   This starts the muse-io server, it is streaming data on port 5000.
-   If you installed MuseLab (which you probably did if you have `muse-io`, you can quickly check the status of your signal)
-   You can now run the `blink.py` script.
-   `blink.py`, by default, does not assume a serial connection with an arduino. Passing the `--serial <port>` argument to the `blink.py` script will setup a serial connection with an _already_ connected arduino device.
-   other default assumptions are that you are streaming osc udp packets on localhost:5000
-   However, if, for some reason you aren't doing the default, you _can_ change the server and port configuration by passing `--ip <ip_address>` and `--port <port_number>` arguments to `blink.py`

