def main():
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        print(i, end=' ')
        for _ in range(3):
            next(numbers)


if __name__ == '__main__':
    main()
