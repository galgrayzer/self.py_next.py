def loop(ditails: dict):
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Last name: ", ditails["last_name"])
        case 2:
            print("Birth month: ", ditails["birth_date"].split(".")[1])
        case 3:
            print("Hobbies: ", ", ".join(ditails["hobbies"]))
        case 4:
            print("Last hobby: ", ditails["hobbies"][-1])
        case 5:
            ditails["hobbies"].append("Cooking")
        case 6:
            print(tuple(ditails["birth_date"].split(".")))
        case 7:
            ditails["age"] = 2024 - int(ditails["birth_date"].split(".")[2])
            print("Age: ", ditails["age"])
        case _:
            print("Invalid choice!")


def main():
    ditails_dict = {"first_name": "Mariah", "last_name": "Carey",
                    "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
    loop(ditails_dict)


if __name__ == '__main__':
    main()
