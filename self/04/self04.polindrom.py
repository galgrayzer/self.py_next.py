def main():
    user_input = input("Enter a string: ").lower().replace(' ', '')
    for i in range(len(user_input) // 2):
        if user_input[i] != user_input[-i - 1]:
            print("NOT")
            break
    else:
        print("OK")


if __name__ == '__main__':
    main()
