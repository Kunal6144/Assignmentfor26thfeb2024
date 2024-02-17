def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons (negative value to exit): "))
        if gallons < 0:
            print("Exiting program.")
            break
        liters = gallons_to_liters(gallons)
        print("{:.2f} gallons is equal to {:.2f} liters.".format(gallons, liters))

if __name__ == "__main__":
    main()
