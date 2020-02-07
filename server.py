import scapy as sc
import csv
teams = []
def setup():
    teamips = input("What is the CSV file containing team info")
    with open(teamips) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                break
            else:
                print(f'Team{row[0]}, OS{row[1]}, ip{row[2]}')

setup()