def mult_tuple(tuple1, tuple2):
    return [(item1, item2) for item1 in tuple1 for item2 in tuple2] + [(item2, item1) for item1 in tuple1 for item2 in tuple2]


def main():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    print(mult_tuple(tuple1, tuple2))


if __name__ == '__main__':
    main()
