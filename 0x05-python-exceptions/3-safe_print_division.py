#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    num = a
    den = b
    try:
        result = num / den
    except ZeroDivisionError:
        return None
    except:
        return None
    finally:
        print("Inside result: {}".format(result) if result in locals() else 
                "Inside result:None")
        if 'result' in locals():
            return result
        else:
            return None
