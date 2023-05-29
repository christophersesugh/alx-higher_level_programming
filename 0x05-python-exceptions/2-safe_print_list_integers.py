#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for elem in my_list:
            if count < x:
                print(my_list["{:d}".format(elem)], end="")
                count += 1
        print()
        return count
    except IndexError:
        print("Out of range")
        return 0
    except ValueError:
        print("Element is not a number")
        return 0

