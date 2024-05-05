def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        for day in range(1, 32):
            yield day
    elif month in [4, 6, 9, 11]:
        for day in range(1, 31):
            yield day
    elif month == 2:
        if leap_year:
            for day in range(1, 30):
                yield day
        else:
            for day in range(1, 29):
                yield day


def gen_years(start=2024):
    while True:
        yield start
        start += 1


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, year % 4 == 0):
                yield "%02d/%02d/%04d" % (day, month, year) + " " + next(gen_time())


def main():
    date = gen_date()
    for _ in range(10):
        print(next(date))
        for _ in range(10000):
            next(date)


if __name__ == '__main__':
    main()
