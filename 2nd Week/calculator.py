n1=float(input("Enter the 1st Number"))
print(f"1st Number is{n1}" )


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2

print("Select Operations")
print(
    "+. Addition\n"
    "-. Subtraction\n"
    "*. Multiplication\n"
    "/. Division\n")

operation = str(input("Enter choice of operation +/-/*//: "))

n2=float(input("Enter the 2nd Number"))
print(f"2nd Number is{n2}" )


if operation == "+":
    print (n1, "+", n2, "=", addition(n1, n2))

elif operation == "-":
    print (n1, "-", n2, "=", subtraction(n1, n2)) 

elif operation == "*":
    print (n1, "*", n2, "=", multiplication(n1, n2)) 
    
elif operation == "/":
    print (n1, "/", n2, "=", division(n1, n2)) 
    
else:
    print("Invalid Input")

