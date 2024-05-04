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

HANGMAN_PHOTOS = {
    1: """
        x-------x
        """,
    2: """
        x-------x
        |
        |
        |
        |
        |
        """,
    3: """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
    4: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
    5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
    6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
    7: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
}

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


def show_hidden_word(secret_word: str, old_letters_guessed: list):
    return " ".join([char if char in old_letters_guessed else "_" for char in secret_word])


def check_win(secret_word, old_letters_guessed):
    return all([char in old_letters_guessed for char in secret_word])


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
    if stage_number in HANGMAN_PHOTOS:
        print(HANGMAN_PHOTOS[stage_number])
    else:
        print("Invalid stage number")


if __name__ == '__main__':
    main()
