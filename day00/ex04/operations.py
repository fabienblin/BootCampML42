import sys

def printUsage() :
    print("Usage: python", sys.argv[0], "<number1> <number2>\n\
Example:\n\tpython", sys.argv[0], "10 3")

if len(sys.argv) < 3 :
    printUsage()
elif len(sys.argv) > 3 :
    print("InputError: too many arguments\n")
    printUsage()
else :
    try :
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("{0:12s} {1:0d}".format("Sum:", num1 + num2))
        print("{0:12s} {1:0d}".format("Difference:", num1 - num2))
        print("{0:12s} {1:0d}".format("Product:", num1 * num2))
        if num2 != 0 :
            print("{0:12s} {1:0f}".format("Quotient:", num1 / num2))
            print("{0:12s} {1:0f}".format("Remainder:", num1 % num2))
        else :
            print("{0:12s} {1:0s}".format("Quotient:", "ERROR (div by zero)"))
            print("{0:12s} {1:0s}".format("Remainder:", "ERROR (modulo by zero)"))
    except ValueError :
        print("InputError: only numbers")
        printUsage()