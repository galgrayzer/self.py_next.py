def is_greater(my_list, n):
    return [num for num in my_list if num > n]


def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)


if __name__ == '__main__':
    main()
