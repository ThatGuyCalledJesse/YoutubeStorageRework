from utils.encode_char import *
from utils.manage_picture import *

with open('example_text.txt') as file:
    input_text = file.read()

encoded = encode(input_text)
create_images(encoded)