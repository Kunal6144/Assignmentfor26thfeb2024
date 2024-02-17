import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    num_sides = int(input("Enter the number of sides on the dice: "))
    roll_result = 0
    while roll_result != num_sides:
        roll_result = roll_dice(num_sides)
        print("You rolled:", roll_result)

if __name__ == "__main__":
    main()
