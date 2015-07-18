#returns the sum of num1 and num2
def add(num1, num2):
    return num1 + num2


#returns the result of subtracting num1 - num2
def sub(num1, num2):
    return num1 - num2


#returns the result of multiplying num1 * num2
def mul(num1, num2):
    return num1 * num2


#returns the result of dividing num1 / num2
def div(num1, num2):
    return num1 / num2


def login():
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    if username == "Zach" and password == "password123":
        print("welcome!")
    elif username == "guest" and password == 'guest':
        print("welcome")
    else:
        print("incorrect")


def main():
    operation = input("What do you wnat to do (+,-,*,/): ")
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        #invalid operation
        print("you must enter a valid operation")
    else:
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        if(operation == '+'):
            print(add(num1, num2))
        elif(operation == '-'):
            print(sub(num1, num2))
        elif(operation == '/'):
            print(div(num1, num2))
        else:
            print(mul(num1, num2))


def end():
    exit1 = input("Would you like to exit? ")
    if (exit1 == 'y'):
        print("goodbye...")
    else:
        main()


login()
main()
end()
