import string

VOWELS = set('aeiou')
CONSONANTS = set(string.ascii_lowercase) - VOWELS | {'ng'}


def char_type(ch):
    if ch in VOWELS:
        return 1
    return 2


def convert(string):
    output = []
    for i, ch in enumerate(string):
        if len(string) == 1:
            other = []
        elif i == 0:
            other = [string[i + 1]]
        elif i == len(string) - 1:
            other = [string[i - 1]]
        else:
            other = [string[i - 1], string[i + 1]]

        if any(char_type(ch) == char_type(o) for o in other):
            output.append(ch.upper())
        else:
            output.append(ch)
    return ''.join(output)


def tokenize(string):
    tokens = string.split('ng')
    output = []
    for i, token in enumerate(tokens):
        for ch in token:
            output.append(ch)
        if i != len(tokens) - 1:
            output.append('ng')
    return output


def main():
    n = int(input())
    for i in range(n):
        line = input()
        tokens = tokenize(line)
        result = convert(tokens)
        print('Case #{}: {}'.format(i + 1, result))


main()
