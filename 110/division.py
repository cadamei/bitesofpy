def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    result = 0
    try:
        result = int(numerator) / int(denominator)
    except ZeroDivisionError:
        print("You can't divide buy zero")
    except TypeError:
        print("You must input a number")
    else:
        if result < 0:
            raise ValueError

    return result
