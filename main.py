def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("Simple Calculator v2")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()

