# Function to add two numbers
def add(x, y):
    """Add two numbers."""
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    """Subtract two numbers."""
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    """Multiply two numbers."""
    return x * y

# Function to divide two numbers
def divide(x, y):
    """Divide two numbers, handling division by zero."""
    if y == 0:
        return "Error! Division by zero is not possible."
    return x / y

# Function to mod two numbers 
def modulation(x, y):
    """Mod two numbers, handling division by zero."""
    if y == 0:
        return "Error! Division by zero is not possible."
    return x % y

# Function to validate if input is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Main function to drive the calculator program
def calculator():
    # Take the first number from the user
    num1 = input("Enter first number: ")
    while not is_number(num1):
        print("Invalid input! Please enter a valid number.")
        num1 = input("Enter first number: ")
    num1 = float(num1)

    # Take the second number from the user
    num2 = input("Enter second number: ")
    while not is_number(num2):
        print("Invalid input! Please enter a valid number.")
        num2 = input("Enter second number: ")
    num2 = float(num2)

    # Display operation options to the user
    print("Operations:")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Divide (/)")
    print("5. Modulation (%)")
    # Take the choice of operation from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    # Perform the chosen operation and show the result
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    elif choice == '5':
        print("Result: ", modulation(num1, num2))
    else:
        print("Invalid Input")

# Execute the calculator program
if __name__ == "__main__":
    calculator()
