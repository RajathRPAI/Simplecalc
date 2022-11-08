# Program make a simple calculator
# This function adds,subtracts,multiplies,divides two numbers
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
print("Select operation(+,-,*,/")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")
while True:
    choice = input("Enter choice(A/B/C/D): ")
    if choice in ('A', 'B', 'C', 'D'):
        num1 = float(input("Enter 1ST NO: "))
        num2 = float(input("Enter 2ND NO: "))

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))
        # For another calculation
        next_calculation = input("Do you want to continue calculation ? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input Pls Check The Inputs You Have Given ")