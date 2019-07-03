MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if int(age) < MIN_DRIVING_AGE:
        print(f'{name} is not allowed to drive')
    else:
        print(f'{name} is allowed to drive')


if __name__ == '__main__':
    allowed_driving('tim', 17)
    allowed_driving('bob', 18)
    allowed_driving('julian', 19)
