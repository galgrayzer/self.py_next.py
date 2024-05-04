from calendar import weekday

DAYS = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]


def main():
    date = input("Enter the date in the format dd/mm/yyyy: ")
    date = date.split("/")
    day = weekday(int(date[2]), int(date[1]), int(date[0]))
    print(DAYS[day])


if __name__ == '__main__':
    main()
