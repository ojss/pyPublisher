"""
Prints data from zmq PULL socket to stdout
"""
import zmq
import sys


def get_socket(host, port):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, "")
    socket.connect('tcp://%s:%s' % (host, port))
    return socket


def print_socket(socket, stdout):
    while 1:
        chunk = socket.recv()
        stdout.write(chunk)
        stdout.flush()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Proxies stdin to PUB socket over zmq')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to connect on')
    parser.add_argument('--port', type=int, default=9900, help='Port to connect to')
    args = parser.parse_args()

    sock = get_socket(args.host, args.port)
    try:
        print_socket(sock, sys.stdout)
    except KeyboardInterrupt:
        sys.exit(0)
