#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    num = a
    den = b
    try:
        result = num / den
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
    except:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
