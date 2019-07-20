names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, item in enumerate(zip(names, countries), 1):
        spaces = ' ' * (11 - len(item[0]))
        print(f'{i}. {item[0]}{spaces}{item[1]}')


if __name__ == '__main__':
    enumerate_names_countries()
