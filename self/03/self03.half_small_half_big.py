def main():
    input_string = input("Enter a string: ")
    print(input_string[:len(input_string) // 2].lower() +
          input_string[len(input_string) // 2:].upper())


if __name__ == '__main__':
    main()
