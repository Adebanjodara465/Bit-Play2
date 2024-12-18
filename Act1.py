def checkIfSame(number1, number2):
    if((number1 ^ number2) != 0):
        print("Numbers are not equal")

    else:
        print("Both numbersa are equal")

number1 = int(input("Enter first your number: ")) 
number2 = int(input("Enter second your number: ")) 
checkIfSame(number1, number2)           