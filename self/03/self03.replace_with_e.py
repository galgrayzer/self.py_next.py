def main():
    user_msg = input("Enter your message: ")
    print(user_msg[0] + user_msg[1:].replace(user_msg[0], 'e'))


if __name__ == '__main__':
    main()
