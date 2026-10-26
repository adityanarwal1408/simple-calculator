
# Simple Calculator
# Created using Python

def calculator():
    print("==============================")
    print("       SIMPLE CALCULATOR")
    print("==============================")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            result = num1 + num2
            operator = "+"

        elif choice == "2":
            result = num1 - num2
            operator = "-"

        elif choice == "3":
            result = num1 * num2
            operator = "*"

        else:
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue

            result = num1 / num2
            operator = "/"

        print(f"Result: {num1:g} {operator} {num2:g} = {result:g}")


if __name__ == "__main__":
    calculator()
