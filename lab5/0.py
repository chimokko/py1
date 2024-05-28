from PIL import Image
from functools import reduce

def invert(pixel):
    return tuple(255 - channel for channel in pixel)

def pixel_generator(image):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            yield image.getpixel((x, y))

def process_image(input_path, output_path):
    with Image.open(input_path) as img:
        inverted_pixels = map(invert, pixel_generator(img))
        
        width, height = img.size
        inverted_img = Image.new("RGB", (width, height))

        for y in range(height):
            for x in range(width):
                inverted_img.putpixel((x, y), next(inverted_pixels))
        
        inverted_img.save(output_path)

input_image_path = input()
output_image_path = 'output_image.png'
process_image(input_image_path, output_image_path)
