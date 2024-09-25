import sys


# Messages
messages = {
    "help": "Usage as follows:\n\t$ python t2b.py <text0> <text1> ... <textn>\n",
    "error": {
        "flag": "invalid flag, try again\n",
    },
}

PAD = 8


def chr2binary(ch: chr):
    return format(ord(ch), "b").zfill(PAD)


def word2binary(word: str):
    return "".join(list(map(chr2binary, word))) + "\n"


def print_binary(word: str):
    sys.stdout.write(word2binary(word))


def split_print(text: str):
    for word in text.split():
        print_binary(word)


def help():
    sys.stdout.write(messages["help"] + "\n")


def error_message():
    sys.stdout.write(messages["error"])


if __name__ == "__main__":

    argv = sys.argv
    idx = 1
    # Check for flags
    if argv[1][0] == "-":
        flag = argv[1][1]
        if flag == "h":
            help()
            sys.exit(0)
        if flag == "s":
            split_print(argv[2])
            sys.exit(0)
        if flag == "p":
            PAD = int(argv[2])
            idx = 3
    for text in argv[idx:]:
        print_binary(text)
    sys.exit(0)
