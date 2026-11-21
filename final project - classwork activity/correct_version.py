#debug this program!
#it should ask user for input and do some math with it

num = int(input("give me an integer: "))
while True:
    operator_num = int(input("give me another integer: "))
    print("a = addition, b = subtraction, c = multiplcation, d = division")
    operation = input("what operation do you want to do: ")

    if operation == "a":
        add = num + operator_num
        print(f"the first number plus the second number is: {add}")

    elif operation == "b":
        subtract = num - operator_num
        print(f"the first number minus the second number is: {subtract}")
    
    elif operation == "c":
        mult = num * operator_num
        print(f"the first number times the second number is: {mult}")
    
    elif operation == "d":
        div = num / operator_num
        print(f"the first number divided by the second number is {div}")
    else:
        print("invalid input, try again")
        break
    
    cont = input("do you want to do another calculation? y/n ")
    if cont == 'n':
        print("goodbye")
        break

    
