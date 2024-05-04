def main():
    temp = input("Enter the temperature you want to convert: ")
    if temp[-1].lower() == 'f':
        celsius = (float(temp[:-1]) - 32) * 5 / 9
        print(f"{celsius}C")
    elif temp[-1].lower() == 'c':
        fahrenheit = float(temp[:-1]) * 9 / 5 + 32
        print(f"{fahrenheit}F")
    else:
        print("Invalid input")
        return


if __name__ == '__main__':
    main()
