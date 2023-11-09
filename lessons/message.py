"""Class to store a message (operator overload, union types, default parameters)."""

class Message:
    to: str
    content: str
    flag: bool

    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False):
        """Constructing a message."""
        self.to = recipient
        self.content = message_content
        self.flag = importance_flag
    
    def __str__(self) -> str:
        """Doctstring again."""
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.flag}\n"
        output += self.content
        # why doesn't output += f' "self.content" ' work?
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(0, factor):
            self.content += " " + copy_val



msg_to_myself: Message = Message("me", "Do your 110 homework!", True)
# msg_to_myself * 100
print(msg_to_myself)


msg_to_camilla: Message = Message("camilla", "You inspire the students!")
print(msg_to_camilla)

# msg_to_bear: Message = Message("Bear")
msg_to_bear: Message = Message(1)
msg_to_bear.content = "Good boy!"
msg_to_bear.important = True
print(msg_to_bear)