# Step 1: Define a function for the calculator
def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Step 2: Take user input
    try:
        operation = int(input("Enter the number corresponding to the operation (1-4): "))
        if operation not in [1, 2, 3, 4]:
            print("Invalid operation. Please choose between 1 and 4.")
            return
        
        # Step 3: Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Step 4: Perform the selected operation
        if operation == 1:
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == 4:
            if num2 == 0:  # Handle division by zero
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers and an integer for the operation.")

# Step 5: Call the calculator function
if __name__ == "__main__":
    calculator()
