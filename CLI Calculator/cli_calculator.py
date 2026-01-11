def add(a: float, b: float):
    return a + b
def subtract(a: float, b: float):
    return a - b
def multiply(a: float, b: float):
    return a*b
def division(a: float, b: float):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


print("Welcome to CLI Calculator")

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice not in [1,2,3,4,5]:
            print("Please enter a number between 1 and 5")
            continue
    except ValueError:
        print("Please enter a whole number")
        continue

    if choice == 5:
        print("Exiting CLI Calculator")
        break
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue
    result = None

    if choice == 1:
        result = add(num1,num2)
        print("Result: ", result)
    elif choice == 2:
        result = subtract(num1,num2)
        print("Result: ", result)
    elif choice == 3:
        result = multiply(num1,num2)
        print("Result: ", result)
    elif choice == 4:
        result = division(num1,num2)
        print("Result: ", result)
 
    if result is not None:
        try:
            data = str(result)
            with open("Output Folder/output.txt", "w") as file:
                file.write(data)
        except TypeError:
            print("Value not a string. Please ensure data written to the file is a string")
            continue
