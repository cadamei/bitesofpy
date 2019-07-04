def sum_numbers(numbers=None):
    # print(f'{numbers} == numbers')
    if numbers is None:
        numbers = range(101)
    else:
        numbers = list(numbers)

    return sum(numbers)


if __name__ == '__main__':
    print(sum_numbers())
    print(sum_numbers(range(1, 11)))
    print(sum([]))