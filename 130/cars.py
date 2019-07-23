from collections import Counter

import requests

CAR_DATA = 'http://projects.bobbelderbos.com/pcc/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

model_year = []


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter()
    for model in data:
        if model['year'] == year:
            cnt[model['automaker']] += 1

    return cnt.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    cars = set()
    for model in data:
        if model['automaker'] == automaker and model['year'] == year:
            cars.add(model['model'])

    return cars


if __name__ == '__main__':
    most_prolific_automaker(1999)
    print(get_models('Volkswagen', 2008))
