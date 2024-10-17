def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("choose operation: ")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input("Enter a number corresponding in your choice (1/2/3/4): ")

if choice == "1":
    result = addition(num1, num2)
    print(f"The result of addition is: {result} ")
elif choice == "2":
    result = subtraction(num1, num2)
    print(f"The result of subtraction is: {result} ")
elif choice == "3":
    result = multiplication(num1, num2)
    print(f"The result of multiplication is: {result} ")
elif choice == "4":
    result = division(num1, num2)
    print(f"The result of division is: {result} ")
else:
    print("error")