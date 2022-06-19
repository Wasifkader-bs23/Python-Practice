from email import message


def print_message(message):
    for x in message:
        print(x)

message=['Hello, world!', 'How are you?']
print_message(message)