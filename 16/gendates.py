from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    t1 = timedelta(days=100)
    t2 = timedelta(days=365)

    time1 = PYBITES_BORN
    time2 = PYBITES_BORN
    while True:
        if time1 + t1 < time2 + t2:
            time1 += t1
            yield time1
        else:
            time2 += t2
            yield time2


if __name__ == '__main__':
    dates = gen_special_pybites_dates()
    for _ in range(10):
        print(next(dates))


# expected = [datetime.datetime(2017, 3, 29, 0, 0),     2017-03-29 00:00:00
#             datetime.datetime(2017, 7, 7, 0, 0),      2017-07-07 00:00:00
#             datetime.datetime(2017, 10, 15, 0, 0),    2017-10-15 00:00:00
#             datetime.datetime(2017, 12, 19, 0, 0),
#             datetime.datetime(2018, 1, 23, 0, 0),     2018-01-23 00:00:00
#             datetime.datetime(2018, 5, 3, 0, 0),      2018-05-03 00:00:00
#             datetime.datetime(2018, 8, 11, 0, 0),     2018-08-11 00:00:00
#             datetime.datetime(2018, 11, 19, 0, 0),    2018-11-19 00:00:00
#             datetime.datetime(2018, 12, 19, 0, 0),
#             datetime.datetime(2019, 2, 27, 0, 0)]     2019-02-27 00:00:00
