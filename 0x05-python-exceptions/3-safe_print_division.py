#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    num = a
    den = b
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return None
    except:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
