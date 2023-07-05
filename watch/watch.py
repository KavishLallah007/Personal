import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        pattern =  re.search(r"(https?:\/\/(?:www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if pattern:
            split = pattern.groups()
            return "https://youtu.be/" + split[1]

...


if __name__ == "__main__":
    main()