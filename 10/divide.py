def positive_divide(numerator, denominator):
    result = 0
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("You can't divide buy zero")
    except TypeError:
        print("You must input a number")
    else:
        if result < 0:
            raise ValueError
    return result


if __name__ == '__main__':
    print(positive_divide([], 2))
