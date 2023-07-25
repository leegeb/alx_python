#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        result = None
    except Exception as e:
        print("An error occurred:", e)
        result = None
    finally:
        print("Inside result: {}".format(result) if result is not None else "Inside result: None")
    return result


