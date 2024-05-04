def numbers_letters_count(my_str):
    out = [0, 0]
    for char in my_str:
        if char.isdigit():
            out[0] += 1
        else:
            out[1] += 1
    return out


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == '__main__':
    main()
