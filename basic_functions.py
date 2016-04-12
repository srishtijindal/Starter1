



"""
CP1404/CP5632 Workshop 04
Basic functions
demonstrating various parameters, returns and the use of a main function
"""
__author__ = 'Lindsay Ward'


def main():
    lowest, highest = get_limits()
    print("lowest =", lowest, "highest =", highest)
    print_between(lowest, highest)


def get_limits():
    """Enter the maximum (10 or above):8
    Maximum too low!
    """
    minimum = int(input("Enter the minimum: "))
    maximum = int(input("Enter the maximum({} or above): ".format(minimum)))
    while True:
        if maximum > minimum:
            break
            print("Maximum too low")
            maximum = int(input("Enter the maximum({} or above): ".format(minimum)))
    return minimum, maximum


def print_between(start, end):
    for i in range(start, end+1):
        print(i, end=' ')

main()
