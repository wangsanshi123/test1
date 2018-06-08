def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # your code here
    def isIllegal(digit):
        return digit == sum([int(item) ** (i + 1) for i, item in enumerate(str(digit))])
        pass

    return [digit for digit in range(a, b + 1) if isIllegal(digit)]

    pass


def encrypt(text, n):
    if text is None or "" or n <= 0:
        return text

    for i in range(n):
        text = "".join(
            [item for i, item in enumerate(text) if i % 2] + [item for i, item in enumerate(text) if not i % 2])
    return text
    pass


def decrypt(encrypted_text, n):
    if encrypted_text is None or "" or n <= 0:
        return encrypted_text

    for i in range(n):
        indice = int(len(encrypted_text) / 2)
        if len(encrypted_text) % 2:
            endchar = encrypted_text[-1]
        else:
            endchar = ''
        encrypted_text = "".join([first + second for first, second in
                                  zip(encrypted_text[indice:],
                                      encrypted_text[:indice])]) + endchar
    return encrypted_text
    pass


def anagrams(word, words):
    # your code here
    return [item for item in words if sorted(word) == sorted(item)]

    pass


def count_smileys(arr):
    return  # the number of valid smiley faces in array/list


def cakes(recipe, available):
    # TODO: insert code
    try:
        return min([available[item] / recipe[item] for item in recipe.keys()])
    except:
        return 0
        pass

    pass

def removNb1(n):
    # your code
    data = range(n+1)
    return [(item1, item2) for item1 in data for item2 in data if item1 * item2 == (sum(data) - item1 -item2)]



def removNb(n):
    sum = n*(n + 1)/2
    return [(x, (sum - x) / (x + 1)) for x in range(1, n+1) if (sum - x) % (x + 1) == 0 and 1 <= (sum - x) / (x + 1) <= n]


if __name__ == '__main__':
    # text = "This is a test!"
    text = "I am yuan tai xing"
    # print(decrypt("This is a test!", 0))
    # print(decrypt("s eT ashi tist!", 2))
    # print(decrypt("This is a test!", 4))
    # print(decrypt("hsi  etTi sats!", 1))


    # from time import clock
    # start = clock()
    # removNb1()
    # finish = clock()
    # print("time:",finish-start)

    print(removNb1(26))

    pass
