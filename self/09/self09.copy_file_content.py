def copy_file_content(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())


def main():
    source = "self/09/utils/copy.txt"
    destination = "self/09/utils/paste.txt"
    copy_file_content(source, destination)


if __name__ == '__main__':
    main()
