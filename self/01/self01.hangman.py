from random import randint


def main():
    # print welcome message
    print_start_phase()

    # print stages in order
    [print_stage(i) for i in range(1, 8)]


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


def print_start_phase():
    WELCOME_MESSAGE = f"""
    Welcome to the game Hangman
        _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/
    {randint(5, 10)}                        """

    print(WELCOME_MESSAGE)


if __name__ == '__main__':
    main()
