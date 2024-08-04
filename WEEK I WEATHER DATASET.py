import csv

file = open('1. Weather Data.csv')
for line in file:
    print(line)

with open('1. Weather Data.csv', 'r') as file:
    weather = csv.reader(file)
    for row in weather:
        print(file)

Type = input("what weather condition do you want to view?").title()
with open('1. Weather Data.csv', 'r') as file:
    weather = csv.reader(file)
    for row in weather:
        if row[7] == (Type):
            print(row)

Speed = input("what wind speed do you want to view?").title()
with open('1. Weather Data.csv', 'r') as file:
    weather= csv.reader(file)
    for row in weather:
        if row[4] == (Speed) :
            print(row)

Condition = input("what weather condition do you want to view?").title()
with open('1. Weather Data.csv', 'r') as file:
    weather= csv.reader(file)
    for row in weather:
        if row[7] == (Condition) :
            print(row)



































