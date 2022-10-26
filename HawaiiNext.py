consonants = ['p', 'k', 'h', 'l', 'm', 'n', 'w']
vowels = {"a": "ah", "e": "eh", "i": "ee", "o": "oh", "u": "oo"}
doubleVowel = {"ai": "eye", "ae": "eye", "ao": "ow", "au": "ow",
               "ei": "ay", "eu": "eh-oo", "iu": "ew", "oi": "oyo",
               "ou": "ow", "ui": "ooey", "iw": "v", "ew": "v", "aw": "w",
               "uw": "w", "ow": "w",
               }

misc = {" ": " ", "'": "'"}
"""
"01234"
"keiki -> kay-kee  X  Kay-ee-kee"
"humuhumunukunukuapua'a"
"""

x = True


class Error(Exception):
    pass


class FalseError(Error):
    # when validation is false
    pass


def validate(word):
    while True:
        try:
            for letter in word:
                y = letter in consonants or letter in vowels or letter in misc
                if y is False:
                    raise FalseError
            return True
        except FalseError:
            return False
            break


def pronounce(word):
    """
    Given a valid hawaiian word,
    returns a string that gives the correct pronunciation
    """
    final = []
    index = 0
    if word[0] == 'i':
        firstVow = vowels[word[0]]
        final.append(firstVow)
    while index < (len(word)):

        by2 = word[index: index + 2]

        if by2 not in doubleVowel:

            if by2[0] in vowels:
                vow = vowels[by2[0]]
                final.append(vow)
                index += 1
            elif by2[0] in misc:
                mis = misc[by2[0]]
                final.append(mis)
                index += 1
            else:
                final.append(by2[0])
                index += 1
        elif by2 in doubleVowel:
            pro = doubleVowel[by2]
            final.append(pro)
            index += 2

        pass

    output = []
    g = 0

    for i in range(len(final)):
        if g > len(final) - 1:
            break
        item = final[g]
        if item in consonants or item == 'v':
            if g + 1 == len(final):
                break
            Vowel = final[g + 1]
            if final.index(item) < final.index(item) + 1:
                output.append(item + Vowel)
                g += 1
        else:
            output.append(item)
        g += 1

    if "'" in output:
        u = output.index("'")
        output[u-1: u+2] = [''.join(output[u-1: u+2])]

    output = ('-'.join(output))

    for ch_ in range(len(output) - 4):
        if output[ch_] == ' ':
            output = output[:ch_ - 1] + ' ' + output[ch_ + 2:]

    return output


while True:
    while True:
        try:
            x = str(input("Your Word Please..  \n"))
            z = x.lower()
            if validate(z) is False:
                raise FalseError
            print(x.upper(), "is pronounced ", pronounce(z))
            break
        except FalseError:
            print('not a hawaii word')
            pass
    inp = input("do you wanna play again? Y/N\n")
    inp = inp.upper()
    if inp[0] == 'Y':
        pass
    elif inp[0] == 'N':
        print('see ya')
        break
