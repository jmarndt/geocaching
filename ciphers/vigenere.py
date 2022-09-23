vigenere_char_vals = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
vigenere_char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(text:str, key:str) -> str:
    return vigenereize(text, key, encrypt=True)


def decrypt(text:str, key:str) -> str:
    return vigenereize(text, key, encrypt=False)


def vigenereize(in_text:str=None, key:str=None, encrypt:bool=True) -> str:
    if key is None:
        return 'No key provided.'
    if in_text is None:
        return 'No text provided.'

    key = key.replace(' ', '').upper()
    key_len = len(key)
    key_itr = 0

    out_text = ''
    for char in in_text:
        char_is_lower = char.islower()
        char = char.upper()
        if char not in vigenere_char_list:
            out_text += char
            continue
        key_char = key[key_itr % key_len]
        char_index = vigenere_char_vals[key_char] + vigenere_char_vals[char] if encrypt else vigenere_char_vals[char] - vigenere_char_vals[key_char]
        cipher_char = vigenere_char_list[char_index % 26]
        out_text += cipher_char.lower() if char_is_lower else cipher_char
        key_itr += 1

    return out_text


def two_sample_analyze(sample_one:str=None, sample_two:str=None) -> dict:
    if sample_one is None or sample_two is None:
        print('You mus provide two samples of the same length')
        return
    sample_one = sample_one.replace(' ', '').upper()
    sample_two = sample_two.replace(' ', '').upper()
    if len(sample_one) != len(sample_two):
        print('You mus provide two samples of the same length')
        return

    spreads = []
    for (char_one, char_two) in zip(sample_one, sample_two):
        index_one = vigenere_char_vals[char_one]
        index_two = vigenere_char_vals[char_two]
        spread = index_two - index_one if index_two > index_one else 26 - (index_one - index_two)
        spreads.append(spread)

    possible_keys = []
    for char in vigenere_char_list:
        possible_key = char
        for spread in spreads:
            latest_char = possible_key[-1]
            next_char = vigenere_char_list[(vigenere_char_vals[latest_char] + spread) % 26]
            possible_key += next_char
        possible_keys.append(possible_key)

    guesses = dict()
    for key in possible_keys:
        guesses[key] = vigenereize(sample_one, key, encrypt=False)

    return guesses