# CSAW 2017 Quals
# Serial
##### Patricia Wilthew -- USF Whitehatter's Computer Security Club
##### misc -- 50 points
## Description

Serial
`nc misc.chal.csaw.io 4239`

## Solution
![Serial1](https://github.com/pwilthew/CTF-Write-Ups/blob/master/CSAW2017-Serial/Serial1.png)

Note that we get 11 bits everytime. The first and the last bits are always 0 and 1. That leaves us with 9 bits. The last of those 9 bits is the parity bit. A serial will be considered correct if the number of ones in the 8 bit string is even and the parity bit is 0, or if the number of ones is odd and the parity bit is 1.

![Serial2](https://github.com/pwilthew/CTF-Write-Ups/blob/master/CSAW2017-Serial/Serial2.png)

![Serial3](https://github.com/pwilthew/CTF-Write-Ups/blob/master/CSAW2017-Serial/Serial3.png)

~~~python
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

        # if a serial is correct, append it to Flag array in ascii respresentation
        if (number_of_ones%2==0 and parity=='0') or (number_of_ones%2==1 and parity=='1'):
            s.send('1\n')
            print "1"
            Flag.append(binascii.unhexlify('%x' % int(serial,2)))

         else: # if a serial has errors, discard it
            s.send('0\n')
            print "0"
            string = (s.recv(512)).strip()
        print ''.join(Flag)

~~~
