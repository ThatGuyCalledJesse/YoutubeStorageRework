from PIL import Image
import math
import os

def create_images(input_list: list, width:int=1920, height:int=1080, folder:str='images'):
    if os.path.exists(folder):
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
    else:
        os.mkdir(folder)
    
    pixel_amount = width * height
    image_amount = math.ceil((len(input_list)/ pixel_amount))
    index = 0

    for i in range(image_amount):
        print(f'Creating images... ({i + 1}/{image_amount})')
        img = Image.new('RGB', (width, height))
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                if index >= len(input_list):
                    pixels[x,y] = (255,255,254)
                else:
                    pixels[x,y] = input_list[index]
                index += 1
        img.save(f'images/picture{i+1}.png')

def decode_images(folder:str='images'):
    images = os.listdir(folder)
    amount_of_files = len(images)