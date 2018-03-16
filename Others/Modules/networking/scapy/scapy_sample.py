# coding=utf-8

import sys
import struct
from scapy.all import *

data = struct.pack('=BHI', 0x12, 20, 1000)
pkt = IP(src='192.168.1.81', dst='192.168.1.10')/UDP(sport=12345,dport=5555)/data
send(pkt, inter=1, count=5)