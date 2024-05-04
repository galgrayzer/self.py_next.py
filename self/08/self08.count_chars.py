def count_chars(my_str: str):
    return {char: my_str.count(char) for char in my_str.lower().replace(' ', '')}


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__ == '__main__':
    main()