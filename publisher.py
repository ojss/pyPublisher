import zmq
import sys
import time

# ZeroMQ Context
context = zmq.Context()


def get_socket(host, port):
    # Define the socket using the "Context"
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://%s:%s' % (host, port))
    time.sleep(0.1)
    return socket


def send_message(sock, file_object, verbose):
    while True:
        for line in file_object:
            message = line
            if verbose:
                print message
            sock.send(message)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Reads a file and publishes it to socket over zmq')
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help="file to read. defaults to stdin")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to listen on')
    parser.add_argument('--port', type=int, default=9900, help='Port to listen on')
    parser.add_argument('--verbose', action='store_true', default=False, help='Print stuff')
    args = parser.parse_args()

    VERBOSE = args.verbose

    sock = get_socket(args.host, args.port)
    send_message(sock, args.input_file, args.verbose)
