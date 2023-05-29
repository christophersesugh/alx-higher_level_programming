#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    num = a
    den = b
    try:
        result = num / den
    except ZeroDivisionError:
        return result
    except:
        return result
    finally:
        print("Inside result: {:d}".format(result))
        return result
