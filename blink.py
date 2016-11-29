import argparse
import serial

from pythonosc import dispatcher
from pythonosc import osc_server


def write_serial(letter):
    if SERIAL:
        arduino.write(letter)
        print(letter)
    else:
        print(letter)

#def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
#        print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)

def blink_handler(unused_addr, args, blink):
    #print("Blink: {}".format(blink))
    if blink:
        write_serial(b'B')

def jaw_handler(unused_addr, args, jaw):
    #print("Jaw Clench: {}".format(jaw))
    if jaw:
        write_serial(b'J')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    parser.add_argument("--serial",
                        default="",
                        help="Arduino serial port")
    args = parser.parse_args()

    if args.serial:
        print ('setting up serial device at %s' % args.serial)
        SERIAL = True
        arduino = serial.Serial(args.serial)
    else: 
        SERIAL = False

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/blink", blink_handler, "Blink")
    dispatcher.map("/muse/elements/jaw_clench", jaw_handler, "Jaw")
#    dispatcher.map("/muse/eeg", eeg_handler, "EEG")


    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
