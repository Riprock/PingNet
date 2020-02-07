import scapy as sc
import csv
teams = []
def setup():
    for i in range(int(input("How many teams are competing?"))):
        teams.append([])
    teamips = input("What is the CSV file containing team info")
    with open(teamips) as file:
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
        lookup = input("What information to pull:")
        try:
            print(teams[int(lookup[0])-1][int(lookup[1])-1])
        except IndexError:
            print("Out of bounds")
        except ValueError:
            print("Why a negative number")
main()