def remove_odd_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]


def main():
    # Create a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to remove odd numbers
    modified_list = remove_odd_numbers(original_list)

    # Print both the original and modified lists
    print("Original list:", original_list)
    print("Cut-down list (without odd numbers):", modified_list)


if __name__ == "__main__":
    main()
