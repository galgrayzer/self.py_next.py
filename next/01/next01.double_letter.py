def double_letter(my_str):
    return ''.join([c * 2 for c in my_str])

def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))

if __name__ == '__main__':
    main()