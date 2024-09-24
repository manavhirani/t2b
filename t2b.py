import os
import sys

messages = {
    "usage": "Usage as follows:\n\t$ python t2b.py <text0> <text1> ... <textn>\n",
    "error": {
        "flag": "invalid flag, try again\n",
    },
}

if __name__ == "__main__":
    # Simple text to binary converter
    # Take the input text(s) as system argument(s)
    # Output the binary representation of each string
    flag = False
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        if arg[0] == "-" and not flag:
            if arg[1] == "h":
                sys.stdout.write(messages["usage"])
                sys.exit(0)
                
            sys.stdout.write(messages["error"]["flag"])
            sys.exit(1)

        flag = True

        def chr2binary(ch: chr, pad=8):
            return format(ord(ch), "b").zfill(pad)

        def text2binary(text: str):
            return "".join(list(map(chr2binary, text))) + "\n"

        sys.stdout.write(text2binary(arg))

    sys.exit(0)