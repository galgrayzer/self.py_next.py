class GreetingCard:
    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        return f"Dear {self._recipient}, I just wanted to say hi. Best, {self._sender}"
    