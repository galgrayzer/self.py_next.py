def who_is_missing(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        numbers = sorted(src.read().split(','))
        for i in range(len(numbers)):
            if int(numbers[i]) + 1 != int(numbers[i + 1]):
                dest.write(str(int(numbers[i]) + 1))
                print(int(numbers[i]) + 1)
                break


def main():
    source = "self/09/utils/numbers.txt"
    destination = "self/09/utils/missing.txt"
    who_is_missing(source, destination)


if __name__ == '__main__':
    main()
