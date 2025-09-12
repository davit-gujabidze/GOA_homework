parent_name = input("Enter your parent's name: ")
user_name = input("Enter your name: ")
print(user_name + " is the child of " + parent_name)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division by zero is not possible")