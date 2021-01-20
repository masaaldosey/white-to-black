from PIL import Image
import numpy as np
import argparse
from pathlib import Path

def black_to_white(path_to_image=None):
    # convert to POSIX path
    path = Path(path_to_image)
    # extract filename
    original_name = path.stem
    # open the image
    image = Image.open(path)
    #convert image to NumPy array
    image_arr = np.array(image)
    # rgb channels
    color_channels = image_arr[:, :, :3]
    # invert the colors
    inverted_color_channels = 255 - color_channels
    # flag for if the image is PNG or JPEG
    is_png = image_arr.shape[2] == 4
    # add the alpha channel back for PNG images
    if is_png:
        alpha_channel = image_arr[:, :, 3]
        inverted_arr = np.dstack( (inverted_color_channels, alpha_channel) )
    else:
        inverted_arr = inverted_color_channels
    # convert NumPy array back to image
    inverted_img = Image.fromarray(inverted_arr)
    # see the converted image
    # inverted_img.show()
    # uncomment the line below to save the converted image
    inverted_img.save(original_name + '_converted' + '.jpeg', 'JPEG')



if __name__=='__main__':
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('imagepath', type=str, default='1.jpeg',
                        help='image to be converted to dark mode')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')

    args = parser.parse_args()
    # answer = args.square**2

    # convert image
    black_to_white(path_to_image=args.imagepath)

    if args.verbose:
        print(f'successfully converted {args.imagepath}')
    else:
        print(f'success')