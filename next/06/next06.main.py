from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    bc = BirthdayCard(25)
    gc = GreetingCard()
    print(bc.greeting_msg())
    print(gc.greeting_msg())


if __name__ == '__main__':
    main()
