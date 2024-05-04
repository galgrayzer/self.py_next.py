from functools import reduce


def sum_of_digits(number):
    return reduce(lambda x, y: x + y, [int(i) for i in str(number)])


def main():
    print(sum_of_digits(104))


if __name__ == '__main__':
    main()
