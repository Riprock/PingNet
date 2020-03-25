from scapy.all import *
import time
rpckt = sr1(IP(dst="1.1.1.1"/ICMP()/"THing"))