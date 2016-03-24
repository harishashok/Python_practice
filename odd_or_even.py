def is_odd(number):
    if number % 2 == 0:
        return False
    return True


def multiple_four(number):
    if number % 4 == 0:
        return True
    return False


def check_point(number, checker):
    if number % checker == 0:
        return True
    return False

if __name__ == "__main__":
    num = int(input("Please enter a number\n"))
    if multiple_four(num):
        print("The number is a multiple of 4")
        if is_odd(num):
            print("%d is odd number" % num)
        else:
            print("%d is even number" % num)

    num = int(input("Please enter a number to check\n"))
    check = int(input("Please enter a number to divide by\n"))

    if check_point(num, check):
        print("%d divides evenly into %d " % (check, num))
    else:
        print("%d not divides evenly into %d " % (check, num))
