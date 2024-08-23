from tqdm import tqdm
import os
from PIL import Image
import numpy as np
from convert import pixel_model

'''
the final images must be 128x128, padded, pixel-locked

1. pad to square
2. pixel lock

what images
diffusion db

take the image, sample color at intervals of width/128
calculate step size then snap to the nearest pixel
'''

def pad(image):
    w, h = image.size
    pad_size = max(w, h)
    result = Image.new(image.mode, (pad_size, pad_size), (0, 0, 0))
    result.paste(image, (0, (w - h) // 2))
    return result

from PIL import Image

def convert_png_to_jpg(image,fill_color=(255, 255, 255)):
    background = Image.new("RGB", image.size, fill_color)

    background.paste(image, (0, 0), image)

    return background

input_path = ".\\data\\pre_images\\"
output_path = ".\\data\\images\\"

model = pixel_model()

count = 1

for filename in tqdm(os.listdir(input_path)):
    with Image.open(input_path + filename) as image:
        image = model.pixelify(image)
        
        if image.mode == 'RGBA':
            #image = convert_png_to_jpg(image)
            pass
        
        image = pad(image)
        image_arr = np.array(image)
        new_image = np.zeros((128, 128, 3), dtype=np.uint8)
        size = image_arr.shape[0]
        step = size / 129

        y = step / 2
        for n in range(128):
            x = step / 2
            y += step
            for i in range(128):
                x += step
                
                xr = round(x)
                yr = round(y)

                new_image[n, i] = image_arr[yr, xr] 

        new_image = Image.fromarray(new_image)

        new_image.save(output_path + "image_" + str(count) + ".jpg" , quality=95)
                
    count += 1