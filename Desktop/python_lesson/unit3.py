def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

def get_input():
    num = int(input("Enter a number: "))
    if num > 0:
        countdown(num)
    elif num < 0:
        countup(num)
    else:
        print("Zero is neutral, try again!")
        get_input()

get_input()
