__codex = {
    'a': (0,0,0),
    'A': (0,0,1),
    'b': (0,0,2),
    'B': (0,0,3),
    'c': (0,0,4),
    'C': (0,0,5),
    'd': (0,0,6),
    'D': (0,0,7),
    'e': (0,0,8),
    'E': (0,0,9),
    'f': (0,0,10),
    'F': (0,0,11),
    'g': (0,0,12),
    'G': (0,0,13),
    'h': (0,0,14),
    'H': (0,0,15),
    'i': (0,0,16),
    'I': (0,0,17),
    'j': (0,0,18),
    'J': (0,0,19),
    'k': (0,0,20),
    'K': (0,0,21),
    'l': (0,0,22),
    'L': (0,0,23),
    'm': (0,0,24),
    'M': (0,0,25),
    'n': (0,0,26),
    'N': (0,0,27),
    'o': (0,0,28),
    'O': (0,0,29),
    'p': (0,0,30),
    'P': (0,0,31),
    'q': (0,0,32),
    'Q': (0,0,33),
    'r': (0,0,34),
    'R': (0,0,35),
    's': (0,0,36),
    'S': (0,0,37),
    't': (0,0,38),
    'T': (0,0,39),
    'u': (0,0,40),
    'U': (0,0,41),
    'v': (0,0,42),
    'V': (0,0,43),
    'w': (0,0,44),
    'W': (0,0,45),
    'x': (0,0,46),
    'X': (0,0,47),
    'y': (0,0,48),
    'Y': (0,0,49),
    'z': (0,0,50),
    'Z': (0,0,51),
    '0': (0,0,52),
    '1': (0,0,53),
    '2': (0,0,54),
    '3': (0,0,55),
    '4': (0,0,56),
    '5': (0,0,57),
    '6': (0,0,58),
    '7': (0,0,59),
    '8': (0,0,60),
    '9': (0,0,61),
    ' ': (0,0,62),
    '!': (0,0,63),
    '@': (0,0,64),
    '#': (0,0,65),
    '$': (0,0,66),
    '%': (0,0,67),
    '^': (0,0,68),
    '&': (0,0,69),
    '*': (0,0,70),
    '(': (0,0,71),
    ')': (0,0,72),
    '-': (0,0,73),
    '_': (0,0,74),
    '=': (0,0,75),
    '+': (0,0,76),
    '[': (0,0,77),
    ']': (0,0,78),
    '{': (0,0,79),
    '}': (0,0,80),
    '|': (0,0,81),
    '\\': (0,0,82),
    ';': (0,0,83),
    ':': (0,0,84),
    '\'': (0,0,85),
    '"': (0,0,86),
    ',': (0,0,87),
    '.': (0,0,88),
    '<': (0,0,89),
    '>': (0,0,90),
    '/': (0,0,91),
    '?': (0,0,92),
    '`': (0,0,93),
    '~': (0,0,94),
}

def get_codex() -> dict:
    return __codex

def __get_values() -> list:
    return list(__codex.values())

def __get_keys() -> list:
    return list(__codex.keys())

def get_key_from_value(value:tuple):
    if value not in __get_values():
        return ('|CharNotRecognized|')
    for key, val in __codex.items():
        if val == value:
            return key

def get_value_from_key(key:str):
    if key not in __get_keys():
        return (255,255,255)
    return __codex.get(key, None)

def encode(input_text:str):
    input_list = list(input_text)
    encoded_list = []

    for char in input_list:
        encoded_list.append(get_value_from_key(char))
    
    return encoded_list

def decode(input_list:list):
    decoded_list = []

    for tuple in input_list:
        decoded_list.append(get_key_from_value(tuple))
    
    decoded_string = ""
    for char in decoded_list:
        decoded_string += char
    
    return decoded_string