import random

def roll_dice(num_dice):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        print("rolled:", roll)
        total += roll
    return total

def main():
    num_dice = int(input(" dice do you want to roll? "))
    total = roll_dice(num_dice)
    print("Total sum of all dice:", total)

if __name__ == "__main__":
    main()
