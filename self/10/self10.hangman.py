from os import path

old_letters = []  # list of old letters guessed

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
    6                        
    
    let's start!"""

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


def main():
    # get file path
    file_path = input("Enter file path: ")

    # check if file path is valid
    if not path.exists(file_path):
        print("Invalid file path")
        return

    # get index
    index = int(input("Enter index: "))

    # print welcome message
    print(HANGMAN_ASCII_ART)
    print_stage(1)
    stage_number = 2

    # choose secret word
    secret_word = choose_word(file_path, index)[1]

    while stage_number < 8:
        # print guess with underscores
        print(show_hidden_word(secret_word, old_letters))

        # get user guess
        user_guess = input("Enter your guess: ").lower()

        # check user guess
        if not try_update_letter_guessed(user_guess, old_letters):
            continue

        if user_guess not in secret_word:
            print(":(")
            print_stage(stage_number)
            stage_number += 1

        if check_win(secret_word, old_letters):
            print("WIN")
            break

        elif stage_number == 8:
            print("LOSE")
            break


def choose_word(file_path, index):
    """
    Choose a word from a file based on the given index.

    Args:
        file_path (str): The path to the file containing the words.
        index (int): The index of the word to choose.

    Returns:
        tuple: A tuple containing the total number of unique words in the file and the chosen word.
    """
    with open(file_path, 'r') as file:
        words = file.read().split()  # read file and split into words
        # return total number of unique words and chosen word
        if index > len(words):
            print("Invalid index")
            exit()
        return (len(set(words)), words[index - 1])


def show_hidden_word(secret_word: str, old_letters_guessed: list):
    """
    Returns a string representation of the secret word, with letters that have been guessed correctly
    shown and letters that haven't been guessed yet replaced with underscores.

    Args:
        secret_word (str): The secret word to be guessed.
        old_letters_guessed (list): A list of letters that have been guessed.

    Returns:
        str: A string representation of the secret word, with guessed letters shown and unguessed
        letters replaced with underscores.
    """
    return " ".join([char if char in old_letters_guessed else "_" for char in secret_word])  # return string with guessed letters shown and unguessed letters replaced with underscores


def check_win(secret_word, old_letters_guessed):
    """
    Check if the player has won the game by guessing all the letters in the secret word.

    Args:
        secret_word (str): The secret word that the player needs to guess.
        old_letters_guessed (list): A list of letters that the player has already guessed.

    Returns:
        bool: True if the player has guessed all the letters in the secret word, False otherwise.
    """
    return all([char in old_letters_guessed for char in secret_word])  # return True if all letters in secret word are in old_letters_guessed, False otherwise


def check_valid_input(guess: str, old_letters_guessed: list):
    """
    Check if the user's guess is valid.

    Parameters:
    guess (str): The user's guess.
    old_letters_guessed (list): A list of previously guessed letters.

    Returns:
    bool: True if the guess is valid, False otherwise.
    """
    if len(guess) < 2 and guess.isalpha() and guess not in old_letters_guessed:  # check if guess is a single letter, is an alphabet letter and not in old_letters_guessed
        return True
    return False


def try_update_letter_guessed(letter_guessed: str, old_letters_guessed: list):
    """
    Tries to update the list of old letters guessed with a new letter.

    Args:
        letter_guessed (str): The letter to be added to the list of old letters guessed.
        old_letters_guessed (list): The list of old letters guessed.

    Returns:
        bool: True if the letter was successfully added to the list, False otherwise.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):  # check if letter_guessed is valid
        # add letter_guessed to old_letters_guessed
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    # print sorted old_letters_guessed
    print(" -> ".join(sorted(old_letters_guessed)))
    return False


def print_stage(stage_number: int):
    """
    Prints the hangman stage corresponding to the given stage number.

    Parameters:
    stage_number (int): The stage number representing the hangman stage.

    Returns:
    None
    """
    if stage_number in HANGMAN_PHOTOS:  # check if stage_number is in HANGMAN_PHOTOS
        # print corresponding hangman stage
        print(HANGMAN_PHOTOS[stage_number])
    else:
        print("Invalid stage number")


if __name__ == '__main__':
    main()
