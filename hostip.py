#!/usr/bin/python3

import socket


def host_ip():
    try:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.connect(('1.1.1.1', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    cuts = '*'*22
    print(cuts)
    print(host_ip())
    print(cuts)
