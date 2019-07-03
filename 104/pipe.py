message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output"""
    split_message = message.split('\n')
    pipe_message = '|'.join(split_message)

    return pipe_message


if __name__ == '__main__':
    print(split_in_columns())
