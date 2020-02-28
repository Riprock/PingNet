import scapy as sc
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
            send.append(input("Command:"))
            send.append(input("CMD Processor:"))
            send.append(input("Target:")) # this is going to use the numbering system that is already in use for organization of the teams and their boxes
            print(send)


main()
#The reason for so many inputs is because I want to see how im going to lay out the command structure. Once that is done
#Im going to be converting it into arguments to condense the program as well as making it easier to use.