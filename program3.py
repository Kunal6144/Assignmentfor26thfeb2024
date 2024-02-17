import random

def roll_dice():
    return random.randint(1, 6)

def main():
    roll_result = 0
    while roll_result != 6:
        roll_result = roll_dice()
        print("You rolled:", roll_result)

if __name__ == "__main__":
    main()
