import string


# a class for the exception when the username contains an illegal character
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, char, index):
        self.username = username
        self.char = char
        self.index = index

    def __str__(self):
        return f"The username '{self.username}' contains the illegal character '{self.char}' at index {self.index}."

# a class for the exception when the username is too short


class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short. It must be at least 3 characters long."


# a class for the exception when the username is too long
class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long. It must be at most 16 characters long."


# a class for the exception when the password is missing a required character
class PasswordMissingCharacter(Exception):
    def __init__(self, password, missing_char):
        self.password = password
        self.missing_char = missing_char

    def __str__(self):
        return f"The password '{self.password}' is missing the required character '{self.missing_char}'."


# a class for the exception when the password is too short
class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short. It must be at least 8 characters long."


# a class for the exception when the password is too long
class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long. It must be at most 40 characters long."


# a function to check the input username and password
def check_input(username, password):
    # check if the username contains any illegal characters
    for i, c in enumerate(username):
        if c not in string.ascii_letters + string.digits + '_':
            raise UsernameContainsIllegalCharacter(username, c, i)

    # check if the password is missing a required character
    # check if the password contains an uppercase letter
    if not any(c.isupper() for c in password):
        raise PasswordMissingCharacter(
            password, 'an uppercase letter')

    # check if the password contains a lowercase letter
    elif not any(c.islower() for c in password):
        raise PasswordMissingCharacter(
            password, 'a lowercase letter')

    elif not any(c.isdigit() for c in password):  # check if the password contains a digit
        raise PasswordMissingCharacter(password, 'a digit')

    # check if the password contains a special character
    elif not any(c in string.punctuation for c in password):
        raise PasswordMissingCharacter(
            password, 'a special character')

    elif len(username) < 3:  # check if the username is too short
        raise UsernameTooShort
    elif len(username) > 16:  # check if the username is too long
        raise UsernameTooLong
    elif len(password) < 8:  # check if the password is too short
        raise PasswordTooShort
    elif len(password) > 40:  # check if the password is too long
        raise PasswordTooLong
    else:
        print("OK")


def main():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong, PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
            print(e)


main()
