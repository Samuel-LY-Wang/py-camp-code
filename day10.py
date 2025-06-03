#Very simple scientific calculator (I WILL NOT ADD GRAPHING IT IS WAY TOO MUCH OF A PAIN IN THE ASS FOR MY CURRENT CODING LEVEL)
import math
def calculate_binary(operation, num1, num2):
    if operation=="+":
        return num1+num2
    if operation=="-":
        return num1-num2
    if operation=="*":
        return num1*num2
    if operation=="/":
        if num2==0:
            return "Invalid Input"
        return num1/num2
    if operation=="max":
        return max(num1,num2)
    if operation=="min":
        return min(num1,num2)
    if operation=="^":
        return num1**num2
    if operation=="log":
        if (num1==1 or num1<=0 or num2<=0):
            return "Invalid Input"
        return math.log(num2)/math.log(num1)

def calculate_unary(operation, num):
    if operation=="exp":
        return math.e ** num
    if operation=="abs":
        return abs(num)
    if operation=="ln":
        if (num <= 0):
            return "Invalid Input"
        return math.log(num)
    if operation=="inv":
        if (num==1):
            return "Invalid Input"
        return 1/num
    if operation=="sin":
        return math.sin(num)
    if operation=="cos":
        return math.cos(num)
    if operation=="tan":
        return math.tan(num)
    if operation=="sec":
        return 1/math.cos(num)
    if operation=="csc":
        return 1/math.sin(num)
    if operation=="cot":
        if (num==0):
            return "Invalid Input"
        return 1/math.tan(num)
    if operation=="asin":
        if (abs(num)>1):
            return "Invalid Input"
        return math.asin(num)
    if operation=="acos":
        if (abs(num)>1):
            return "Invalid Input"
        return math.acos(num)
    if operation=="atan":
        return math.atan(num)

binary_operations=["+", "-", "*", "/", "^", "max", "min", "log"]
unary_operations=["exp", "abs", "ln", "inv", "sin", "cos", "tan", "sec", "csc", "cot", "asin", "acos", "atan"]
operations=binary_operations + unary_operations
print("This is the calculator")
while True:
    print("What operation? Here are currently supported operations:")
    print(*operations, sep="\n")
    op=input("")
    if (op not in operations):
        print("That operation is not supported yet. Please try again.")
        continue
    if op in binary_operations:
        inputs=2
    else:
        inputs=1
    if inputs==1:
        inputnum=float(input("What is your input?\n"))
        outnum=calculate_unary(op, inputnum)
        if (outnum == "Invalid Input"):
            print("Invalid Input, please try again")
            continue
        print(f"The result is: {outnum}")
        again=input("Do you want to do another operation? (yes/no)\n").lower()
        if (again != "yes"):
            print("Thanks for using the calculator!")
            break
    else:
        inputnum1=float(input("What is your first input?\n"))
        inputnum2=float(input("What is your second input?\n"))
        outnum=calculate_binary(op, inputnum1, inputnum2)
        if (outnum == "Invalid Input"):
            print("Invalid Input, please try again")
            continue
        print(f"The result is: {outnum}")
        again=input("Do you want to do another operation? (yes/no)\n").lower()
        if (again != "yes"):
            print("Thanks for using the calculator!")
            break