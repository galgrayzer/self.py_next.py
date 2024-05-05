def longest_name(file_path):
    with open(file_path, 'r') as file:
        return max(file.read().splitlines(), key=len)


def sum_lens(file_path):
    with open(file_path, 'r') as file:
        return sum(len(line.strip()) for line in file)


def print_shortest(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        print("\n".join([line for line in lines if len(
            line) == len(min(lines, key=len))]))


def create_length_file(src, dest):
    with open(src, 'r') as src_file, open(dest, 'w') as dest_file:
        [dest_file.write(f'{len(line.strip())}\n') for line in src_file]


def get_words(file_path, length):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if len(line.strip()) == length]


def main():
    longest = longest_name('next/01/utils/names.txt')
    print(f'Longest name: {longest}')

    total_len = sum_lens('next/01/utils/names.txt')
    print(f'Total length: {total_len}')

    print_shortest('next/01/utils/names.txt')

    create_length_file('next/01/utils/names.txt', 'next/01/utils/lengths.txt')

    length = int(input("Enter length: "))
    print(get_words('next/01/utils/names.txt', length))


if __name__ == '__main__':
    main()
