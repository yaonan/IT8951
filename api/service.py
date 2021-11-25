from IT8951 import constants
from PIL import Image, ImageDraw, ImageFont
from sys import path
path += ['../../']

def clear_display(display):
    print('Clearing display...')
    display.clear()

def display_image_8bpp(display, file):
    img_path = 'images/2.png'
    print('Displaying "{}"...'.format(img_path))

    # clearing image to white
    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))

    img = Image.open(file)

    # TODO: this should be built-in
    dims = (display.width, display.height)

    img.thumbnail(dims)
    paste_coords = [dims[i] - img.size[i] for i in (0,1)]  # align image with bottom of display
    display.frame_buf.paste(img, paste_coords)

    display.draw_full(constants.DisplayModes.GC16)