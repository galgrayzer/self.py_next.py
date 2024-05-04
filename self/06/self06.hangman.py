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

old_letters = []


def main():
    # print welcome message
    print(HANGMAN_ASCII_ART)

    # print stages in order
    # [print_stage(i) for i in range(1, 8)]

    # get user guess
    user_guess = input("Enter your guess: ")

    # check user guess
    check_valid_input(user_guess)

    # convert user guess to lowercase
    user_guess = user_guess.lower()

    print(user_guess)

    # print guess with underscores
    print_guess(user_guess)


def check_valid_input(guess: str, old_letters_guessed: list):
    if len(guess) < 2 and guess.isalpha() and guess not in old_letters_guessed:
        return True
    return False


def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    print(" -> ".join(old_letters_guessed.sort()))
    return False


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
