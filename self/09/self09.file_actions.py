def sort(file: str):
    with open(file, 'r') as f:
        words = list(set(f.read().split(' ')))
        return sorted(words)


def rev(file: str):
    with open(file, 'r') as f:
        return "\n".join([line[::-1] for line in f.readlines()])


def last(file: str, n: int):
    with open(file, 'r') as f:
        return "\n".join(f.readlines()[n:])


def main():
    file_path = input("Enter file path: ")
    action = input("Enter action: ")
    match action:
        case "sort":
            print(sort(file_path))

        case "rev":
            print(rev(file_path))

        case "last":
            n = int(input("Enter a number: "))
            print(last(file_path, n))

        case _:
            print("Not a valid option")


if __name__ == '__main__':
    main()
