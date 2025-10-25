result = 0


def main():
    print("\n\t***CALCULATOR APP***")
    print("\tby @PAYAL RAMDAS SUNE\n")
    while True:
        # choices for user
        print("1.ADDITION")
        print("2.SUBTRACTION")
        print("3.MULTIPLICATION")
        print("4.DIVISION")
        print("5.MODULUS")
        print("6.FLOOR DIVISION")
        print("7.POWER")
        print("8.EXIT")
        # taking input from the user
        choice = int(input("\nEnter your Choice : "))
        # for exiting
        if (choice == 8):
            print("\n\n")
            break
        elif (choice > 8):
            print("\nINVALID CHOICE , PLEASE TRY AGAIN LATER\n")
        else:
            a = float(input("\nEnter the first Number : "))
            b = float(input("Enter the Second Number : "))

            if (choice == 1):
                add(a, b)
            elif (choice == 2):
                sub(a, b)
            elif (choice == 3):
                mul(a, b)
            elif (choice == 4):
                div(a, b)
            elif (choice == 5):
                mod(a, b)
            elif (choice == 6):
                flr(a, b)
            elif (choice == 7):
                power(a, b)
            elif (choice == 8):
                break;
            else:
                print("\nINVALID CHOICE , PLEASE TRY AGAIN LATER\n")




# add() method
def add(n, m):
    result = n + m
    print(f"\nAddition of {n} and {m} is : {result}")


# sub() method
def sub(n, m):
    result = n - m
    print(f"\nSubtraction of {n} and {m} is : {result}")


# mul() method
def mul(n, m):
    result = n * m
    print(f"\nMultiplication of {n} and {m} is : {result}")


# div() method
def div(n, m):
    if (m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n / m
        print(f"\nDivision of {n} and {m} is : {result}")


# mod() method
def mod(n, m):
    if (m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n % m
        print(f"\nModulus of {n} and {m} is : {result}")


# flr() method
def flr(n, m):
    if (m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n // m
        print(f"\nFloor Division of {n} and {m} is : {result}")


# power() method
def power(n, m):
    result = n ** m
    print(f"\n{n} to the Power of {m} is : {result}")


# main function
if __name__ == "__main__":
    main()