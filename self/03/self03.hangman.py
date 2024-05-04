# global welcome message constant
HANGMAN_ASCII_ART = f"""
    Welcome to the game Hangman
        _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/
    6                        """


def main():
    # print welcome message
    print(HANGMAN_ASCII_ART)

    # print stages in order
    # [print_stage(i) for i in range(1, 8)]

    # get user guess
    user_guess = input("Enter your guess: ").lower()
    print(user_guess)

    # print guess with underscores
    print_guess(user_guess)


def print_guess(word: str):
    [print("_", end=" ") for _ in word]


def print_stage(stage_number: int):
    match stage_number:
        case 1:
            print("""
                  x-------x
                    """)
        case 2:
            print("""
                  x-------x
                  |
                  |
                  |
                  |
                  |
                    """)

        case 3:
            print("""
                  x-------x
                  |       |
                  |       0
                  |
                  |
                  |
                    """)

        case 4:
            print("""
                  x-------x
                  |       |
                  |       0
                  |       |
                  |
                  |
                    """)

        case 5:
            print("""
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |
                  |
                    """)

        case 6:
            print("""
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |      /
                  |
                    """)

        case 7:
            print("""
                  x-------x
                  |       |
                  |       0
                  |      /|\\
                  |      / \\
                  |
                    """)

        case _:
            print("Invalid stage number. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()
