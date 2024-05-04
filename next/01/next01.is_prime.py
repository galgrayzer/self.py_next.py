def is_prime(number):
    return not bool([i for i in range(2, number) if number % i == 0])


def main():
    print(is_prime(42))
    print(is_prime(43))


if __name__ == '__main__':
    main()
