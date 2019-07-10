

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    list = [number for number in numbers if number % 2 == 0 and number > 0]

    return list


print(filter_positive_even_numbers(list(range(-10, 11))))
