caesar_char_vals = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
caesar_char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(text:str, rotation:int) -> str:
    return caesarize(text, rotation, encrypt=True)


def decrypt(text:str, rotation:int) -> str:
    return caesarize(text, rotation, encrypt=False)


def caesarize(in_text:str=None, rotation:int=None, encrypt:bool=True) -> str:
    if rotation is None:
        return 'No rotation key provided.'
    if in_text is None:
        return 'No text provided.'

    out_message = ''
    for char in in_text:
        is_lower = char.islower()
        if char.upper() not in caesar_char_list:
            out_message += char
            continue
        char_idx = caesar_char_vals[char.upper()]
        rot_idx = (char_idx + rotation) % 26 if encrypt else (char_idx - rotation) % 26
        rot_char = caesar_char_list[rot_idx]
        out_message += rot_char.lower() if is_lower else rot_char

    return out_message


def caesar_analyze(text:str=None) -> dict:
    if text is None:
        print('No text provided.')
        return

    text_rotations = dict()
    for rotation in range(1,26):
        text_rotations[rotation] = caesarize(text, rotation)

    return text_rotations