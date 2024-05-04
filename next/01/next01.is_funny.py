def is_funny(string):
    return not bool([char for char in string if char not in 'ah'])


def main():
    print(is_funny("hahaahahaha"))


if __name__ == '__main__':
    main()
