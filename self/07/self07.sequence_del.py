def sequence_del(my_str):
    return "".join([char for idx, char in enumerate(my_str) if idx == 0 or my_str[idx - 1] != char])


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))


if __name__ == '__main__':
    main()
