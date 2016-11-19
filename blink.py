import argparse
import serial

from pythonosc import dispatcher
from pythonosc import osc_server


def blink_handler(unused_addr, args, blink):
    print("Blink: {}".format(blink))
    ser.write('B')


def jaw_handler(unused_addr, args, jaw):
    print("Jaw Clench: {}".format(jaw))
    ser.write('J')

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
        arduino = serial.Serial(args.serial)

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/blink", blink_handler, "Blink")
    dispatcher.map("/muse/elements/jaw_clench", jaw_handler, "Jaw")


    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
