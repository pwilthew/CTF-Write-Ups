#!/usr/bin/env python2
from pwn import *
import socket 
import binascii
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 4239))

#r = remote("misc.chal.csaw.io", 4239)

msg = s.recv(512)

string = (msg.splitlines()[1]).strip()
Flag = []

while True:
    print "String",string
    serial = string[1:9]
    parity = string[9]
    print "Serial",serial
    number_of_ones = serial.count('1')

    if (number_of_ones%2==0 and parity=='0') or (number_of_ones%2==1 and parity=='1'):
        s.send('1\n')
        print "1"
        Flag.append(binascii.unhexlify('%x' % int(serial,2)))

    else:
        s.send('0\n')
        print "0"

    string = (s.recv(512)).strip()
    print ''.join(Flag)
