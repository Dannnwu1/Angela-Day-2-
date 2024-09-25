import os


def tip_caculator():
    print("Welcome to the tip caculator.")
    bill = float(input('What was the total bill? $ '))
    percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    people = int(input('How many people to split the bill? '))
    amount = round((bill * (1 + percentage / 100)) / people, 2)
    print("Each person should pay: $" + "{:.2f}".format(amount))
    # Clearing the Screen
    os.system('cls')


while True:
    tip_caculator()
