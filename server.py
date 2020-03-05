from scapy.all import *
import csv
teams = []
cmdproc = [["l", "wsl"], ["p", "powershell"], ["c", "cmd"]]
def setup():
    #int(input("How many teams are competing?"))
    for i in range(15):
        teams.append([])
    #teamips = input("What is the CSV file containing team info")
    with open("teams.txt") as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                break
            else:
                teams[int(row[0]) - 1].append([row[1], row[2]])
    print(teams)
    #Fork Point is here.

def sniffer():
    pkts = sc.sniff(filter="icmp and host 66.35.250.151")
    #These packets will come in periodically. The heartbeat will just have 1pkt that will have the str hb

def main():
    setup()
    print("Welcome to PingNet")
    while True:
        cmd = input("Pingnet:")
        if cmd == "exit":
            print("Closing")
            break
        elif cmd == "lookup":
            lookup = input("What information to pull:")
            try:
                print(teams[int(lookup[0])-1][int(lookup[1])-1])
            except IndexError:
                print("Out of bounds")
            except ValueError:
                print("Why a negative number")
        elif cmd == "send":
            send = []
            send.append(input("CMD Processor:"))
            send.append(input("Command:"))
            target = input("Target:") # this is going to use the numbering system that is already in use for organization of the teams and their boxes
            print(send)
            msg = ''.join(send)
            print(msg)
            print(teams[int(target[0])-1][int(target[1])-1][1])
            rpckt = sr1(IP(dst=teams[int(target[0])-1][int(target[1])-1][1])/ICMP()/msg)
            print(rpckt.show())

main()
#The reason for so many inputs is because I want to see how im going to lay out the command structure. Once that is done
#Im going to be converting it into arguments to condense the program as well as making it easier to use.