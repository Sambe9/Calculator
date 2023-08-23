#ADDITION
def add(x, y):
    return x + y

#SUBRACTION
def subtract(x, y):
    return x - y

#MULTIPLICATION
def multiply(x, y):
    return x * y

#DIVIDE
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

#OPERATION
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#CHOOSE OPERATION
choice = input("Enter choice (1/2/3/4): ")

#ENTER VALUE (1)
num1 = float(input("Enter first number: "))
#ENTER VALUE (2)
num2 = float(input("Enter second number: "))

#IF ELSE CONDTION FOR GETTING FINAL OUTPUT
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")
