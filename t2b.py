import sys


# Messages
messages = {
    "usage": "Usage as follows:\n\t$ python t2b.py <text0> <text1> ... <textn>\n",
    "error": {
        "flag": "invalid flag, try again\n",
    },
}


def chr2binary(ch: chr, pad=8):
    return format(ord(ch), "b").zfill(pad)


def text2binary(text: str):
    return "".join(list(map(chr2binary, text))) + "\n"


if __name__ == "__main__":

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        if i == 1 and arg[0] == "-":  # Check if there's a flag
            if arg[1] == "h":  # Help flag
                sys.stdout.write(messages["usage"])
                sys.exit(0)

            sys.stdout.write(messages["error"]["flag"])
            sys.exit(1)

        sys.stdout.write(text2binary(arg))

    sys.exit(0)
