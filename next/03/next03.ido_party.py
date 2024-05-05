class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"under 18, can come in {18 - self.age} years"


def send_invitation(name, age):
    if int(age) < 18:
        try:
            raise UnderAge(age)
        except UnderAge as e:
            print(f"UnderAge: {e}")
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation('Alice', 17)
    send_invitation('Bob', 20)


if __name__ == '__main__':
    main()
