def last_early(my_str: str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    return last_char in my_str[:-1]


def main():
    print(last_early("happy birthday"))
    print(last_early("best of luck"))
    print(last_early("Wow"))
    print(last_early("X"))


if __name__ == '__main__':
    main()
