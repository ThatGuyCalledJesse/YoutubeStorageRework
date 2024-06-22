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

        for y in range(height):
            for x in range(width):
                if index >= len(input_list):
                    pixels[x,y] = (255,255,254)
                else:
                    pixels[x,y] = input_list[index]
                index += 1
        img.save(f'images/image{i+1}.png')

def decode_images(folder:str='images'):
    images = os.listdir(folder)
    amount_of_files = len(images)
    index:int = 1

    for _ in range(amount_of_files):
        img = Image.open(f'{folder}/image{i}.png')
        WIDTH:int = img.width
        HEIGHT:int = img.height
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pixel = 0
        index += 1