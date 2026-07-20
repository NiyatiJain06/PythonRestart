# Mini Calculator Project 
# Create 3 function

def addFunc(a, b):
    print(f"Result {a + b}")
def subtractFunc(a, b):
    print(f"Result {a - b}")
def multiplyFunc(a, b):
    print(f"Result {a * b}")

# get input to a user

print("____Mini Calculator Project____")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))    
print("Choose the Oprations : 1. add, 2. subtract, 3. multiply")
choice = input("Enter 1, 2, or 3:")

# user choice (the logic)

if choice == '1':
    addFunc(num1, num2)
elif choice == '2':
    subtractFunc(num1, num2)
elif choice == '3':
    multiplyFunc(num1, num2)
else:
    print("Invalide choice! Please run again.") 