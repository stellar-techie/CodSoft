#SIMPLE CALCULATOR

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Exponent(x, y):
    return x ** y

def main():
    print("Simple Calculator")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nSelect the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Error! Division by zero is not allowed.")
    elif choice == '5':
        print(f"The result is: {Exponent(num1, num2)}")

    else:
        print("Invalid input! Please enter a valid choice.")

if __name__ == "__main__":
    main()
