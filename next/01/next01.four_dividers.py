def four_dividers(number):
    return [i for i in range(1, number + 1) if i % 4 == 0]


def main():
    print(four_dividers(9))
    print(four_dividers(3))


if __name__ == '__main__':
    main()
