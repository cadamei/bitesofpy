def positive_divide(numerator, denominator):
    result = 0
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("You can't divide buy zero")
    except TypeError:
        print("You must input a number")
    elif numerator or denominator is None:
            raise ValueError
    elif result < 0:
            raise ValueError
    finally:
        return result


if __name__ == '__main__':
    print(positive_divide([], 2))
