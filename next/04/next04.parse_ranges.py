def parse_ranges(ranges_string):
    ranges = (r for r in ranges_string.split(','))
    numbers = (list(range(int(r.split('-')[0]),
               int(r.split('-')[1]) + 1)) for r in ranges)
    out = (n for number in numbers for n in number)
    return out


def main():
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == '__main__':
    main()
