from utils import *

with open('example_text.txt') as file:
    input_text = file.read()

encoded = encode(input_text)
create_images(encoded, width=100, height=100)
print(1)
decoded = decode(decode_images())
print(decoded)