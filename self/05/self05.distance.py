def distance(num1, num2, num3):
    if abs(num1 - num2) == 1 or abs(num1 - num3) == 1:
        if (abs(num2 - num1) > 1 and (num2 - num3) > 1) or (abs(num3 - num1) > 1 and abs(num3 - num2) > 1) or (abs(num1 - num3) > 1 and abs(num2 - num1) > 1):
            return True
    return False


def main():
    print(distance(1, 2, 10))
    print(distance(4, 5, 3))


if __name__ == '__main__':
    main()
