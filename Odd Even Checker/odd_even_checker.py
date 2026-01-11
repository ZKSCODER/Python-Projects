def checker():
    while True:
        try:
            num = input("Enter a number: ")
            remainder = int(num) % 2 #Converts a string to an integer an checks if it is even (0) or odd (not 0)
            if remainder == 0:
                return num, "even"
            else:
                return num, "odd"
        except ValueError:
            print("Invalid input. Please enter whole numbers only")
            continue

num, result = checker()
print(f"The number {num} is {result}")    