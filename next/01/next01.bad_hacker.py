def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(''.join([chr(ord(char) + 2)
          for char in password]).replace('"', ' ').replace("<", ":"))


if __name__ == '__main__':
    main()
