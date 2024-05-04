def arrow(my_char, max_length):
    out = ""
    for i in range(max_length):
        out += my_char * (i + 1) + "\n"
    for i in range(max_length - 1):
        out += my_char * (max_length - i - 1) + "\n"
    return out


def main():
    print(arrow("*", 5))


if __name__ == '__main__':
    main()
