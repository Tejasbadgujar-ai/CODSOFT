# ================================
# CALCULATOR APPLICATION
# ================================
# This program allows the user to:
# 1. Input two numbers
# 2. Choose an operation (+, -, *, /)
# 3. Display the result

print("\n--- CALCULATOR ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, //): ") # Changed from "/" to "//" for integer division

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")