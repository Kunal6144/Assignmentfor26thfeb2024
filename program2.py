def main():
    cities = []  # Initialize an empty list to store the city names

    # Use a for loop to ask the user to enter the names of five cities
    for i in range(5):
        city = input("Enter the name of city {}: ".format(i+1))
        cities.append(city)  # Add the city to the list

    print("\nList of cities:")
    # Use a for/in loop to iterate through the list and print each city
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()
