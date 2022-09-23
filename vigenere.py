from dataclasses import dataclass
from enum import Enum

char_vals = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class CipherType(Enum):
    vigenere: str = 'vigenere'


@dataclass
class Cipher:
    cipher_type: CipherType
    cipher_key: str = None
    cipher_text: str = None
    plain_text: str = None


def vigenere(cipher: Cipher, keep_spaces=True, keep_case=False) -> Cipher:
    cipher.cipher_key = cipher.cipher_key.replace(' ', '').upper()
    key_len = len(cipher.cipher_key)
    key_itr = 0
    encrypt = True if cipher.plain_text != None and cipher.cipher_text == None else False
    in_text = cipher.plain_text if encrypt else cipher.cipher_text
    out_text = ''

    for char in in_text:
        char_is_lower = char.islower()
        char = char.upper()
        if char == ' ' and keep_spaces:
            out_text += char
            continue
        if (char == ' ' and not keep_spaces) or char not in char_list:
            continue
        key_char = cipher.cipher_key[key_itr % key_len]
        char_index = char_vals[key_char] + char_vals[char] if encrypt else char_vals[char] - char_vals[key_char]
        cipher_char = char_list[char_index % 26]
        out_text += cipher_char.lower() if (keep_case and char_is_lower) else cipher_char
        key_itr += 1

    if encrypt:
        cipher.cipher_text = out_text
    else:
        cipher.plain_text = out_text

    return cipher


def key_guesser(samp_one: str, samp_two: str):
    if len(samp_one) != len(samp_two): return 'Samples lengths not equal'
    sample_one = samp_one.replace(' ', '').upper()
    sample_two = samp_two.replace(' ', '').upper()

    spreads = []
    for (char_one, char_two) in zip(sample_one, sample_two):
        index_one = char_vals[char_one]
        index_two = char_vals[char_two]
        spread = index_two - index_one if index_two > index_one else 26 - (index_one - index_two)
        spreads.append(spread)

    possible_keys = []
    for char in char_list:
        possible_key = char
        for spread in spreads:
            latest_char = possible_key[-1]
            next_char = char_list[(char_vals[latest_char] + spread) % 26]
            possible_key += next_char
        possible_keys.append(possible_key)

    for key in possible_keys:
        cipher = Cipher(CipherType.vigenere, cipher_key=key, cipher_text=samp_one)
        cipher = vigenere(cipher)
        print(f'Key: {cipher.cipher_key}')
        print(f'Sample one plain text: {cipher.plain_text}\n')


if __name__ == '__main__':
    sample1 = 'ADLNHEJLQKOD'
    sample2 = 'KLGFWTSGNSMM'
    key_guesser(sample1, sample2)
    
    attack = Cipher(CipherType.vigenere, cipher_key='Lemon', plain_text='Attack At Dawn')
    print(vigenere(attack))
    
