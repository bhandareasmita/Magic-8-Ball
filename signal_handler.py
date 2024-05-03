import signal
import sys


def signal_handler(sig, frame):
    print('Signal received:', sig)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

print("Running... Press Ctrl+C to trigger the signal handler.")

while True:
    pass
