from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0):
        self._sender_age = sender_age
        super().__init__()

    def greeting_msg(self):
        return f"Happy Birthday {self._recipient}! You are {self._sender_age} years old today. Best, {self._sender}"
