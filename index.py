import argparse


def encode(text: str):
    target = ""
    for x in range(len(text)):
        if text[x] == "-":
            target += "-"
            continue
        ans = (ord(text[x])-20)
        target += chr(ans)
    return target

def decode(text: str): 
    target = ""
    for x in range(len(text)):
        if text[x] == "-":
            target += "-"
            continue
        ans = (ord(text[x])+20)
        target += chr(ans)
    return target

def main(text, option):
    if option == "1":
        return encode(text=text)
    if option == "2":
        return decode(text=text)

args = argparse.ArgumentParser(prog="pyencode", description="pyencode scrambles a giving string in the cli and it can also decode encoded strings")
args.add_argument("-t", "--text", help="--text is the string you want to encode or decode")
args.add_argument("-c", "--choice", help="--choice is the choice between encoding and decoding, 1 is encoding and 2 is decoding")

parser = args.parse_args()
print(main(parser.text, parser.choice))