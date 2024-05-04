def are_lists_equal(list1: list, list2: list):
    list1.sort(), list2.sort()
    return list1 == list2


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))


if __name__ == '__main__':
    main()
