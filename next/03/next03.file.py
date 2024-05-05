def read_file(file_name):
    out_str = ''
    try:
        file = open(file_name, 'r')
        out_str = f"""
        __Content_Start__
        {file.read()}
        __Content_End__
        """
    except FileNotFoundError:
        out_str = f"""
        __Content_Start__
        __NO_SUCH_FILE__
        __Content_End__
        """
    else:
        file.close()
    finally:
        return out_str


def main():
    print(read_file('next/01/utils/names.txt'))
    print(read_file('next/01/utils/names2.txt'))


if __name__ == '__main__':
    main()
