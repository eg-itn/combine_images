"""
combine images
"""

import argparse
import os
import sys
import traceback
from PIL import Image


AVAILABLE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp']


def main(args):
    """main function"""
    try:
        if not os.path.exists(args.inputdir):
            sys.exit('input directory does not exist')

        # define output directory
        if args.outputdir is None:
            args.outputdir = args.inputdir
        if not os.path.exists(args.outputdir):
            os.makedirs(args.outputdir)

        # open all images in folder
        images = []
        for x in os.listdir(args.inputdir):
            _fname, ext = os.path.splitext(x)
            if ext.lower() in AVAILABLE_EXTENSIONS:
                images.append(Image.open(os.path.join(args.inputdir, x)))

        # combine images into a grid
        # calculate grid size
        grid_width = args.grid_width
        grid_height = args.grid_height
        if grid_width == 0 and grid_height == 0:
            sys.exit('grid_width and grid_height cannot both be 0')
        elif grid_width == 0:
            grid_width = (len(images) // grid_height) + int(len(images) % grid_height != 0)
        elif grid_height == 0:
            grid_height = (len(images) // grid_width) + int(len(images) % grid_width != 0)

        # TODO: 画像サイズが異なる場合の処理が必要
        grid = Image.new('RGB', (grid_width * images[0].width, grid_height * images[0].height))
        for i, image in enumerate(images):
            grid.paste(image, (i % grid_width * image.width, i // grid_width * image.height))

        # save grid
        grid.save(os.path.join(args.outputdir, 'grid.jpg'))
    except Exception:
        traceback.print_exc()


argparser = argparse.ArgumentParser(description='combine images')
argparser.add_argument('inputdir', type=str, help='input directory')
argparser.add_argument('grid_width', type=int, help='if 0, calculated from grid_height')
argparser.add_argument('grid_height', type=int, help='if 0, calculated from grid_width')
argparser.add_argument('--outputdir', type=str, help='output directory', default=None)

main(argparser.parse_args())
