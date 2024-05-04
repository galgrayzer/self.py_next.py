def chocolate_maker(small, big, x):
    return x % 5 <= small and x // 5 <= big


def main():
    print(chocolate_maker(3, 1, 8))
    print(chocolate_maker(3, 1, 9))
    print(chocolate_maker(3, 2, 10))


if __name__ == '__main__':
    main()
