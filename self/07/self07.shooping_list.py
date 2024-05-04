def loop(shooping_list):
    while True:
        choice = int(input("Please enter a number between 1 and 9: "))
        match choice:
            case 1:
                print("Your shooping list is: ", shooping_list)
            case 2:
                print("You have", len(shooping_list),
                      "items in your shooping list.")
            case 3:
                item = input("What item would you like to search for? ")
                if item in shooping_list:
                    print("Yes,", item, "is in your shooping list.")
                else:
                    print("No,", item, "is not in your shooping list.")
            case 4:
                item = input("What item would you like to search for? ")
                print("You have", shooping_list.count(
                    item), item, "in your shooping list.")
            case 5:
                item = input(
                    "What item would you like to remove from your shooping list? ")
                if item in shooping_list:
                    shooping_list.remove(item)
                    print(item, "has been removed from your shooping list.")
                else:
                    print(item, "is not in your shooping list.")
            case 6:
                item = input(
                    "What item would you like to add to your shooping list? ")
                shooping_list.append(item)
                print(item, "has been added to your shooping list.")
            case 7:
                print("Invalid items are:", [
                      item for item in shooping_list if not item.isalpha() or len(item) < 3])
            case 8:
                shooping_list = list(set(shooping_list))
                print("Your shooping list has been deduplicated.")
            case 9:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, please enter a number between 1 and 9.")


def main():
    shooping_list = input("Please enter your shooping list: ").split(",")
    loop(shooping_list)


if __name__ == '__main__':
    main()
