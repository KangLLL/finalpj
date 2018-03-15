import os
import sys
import shutil
from PIL import Image
from resizeimage import resizeimage

def resize_file(csv_file, target_dir, target_size):
    with open('./train.csv') as f:
        lines = f.read().splitlines()
        del lines[0]
        for i in range(len(lines)):
            row = lines[i].split(',')
            file_path = os.path.join(target_dir, row[0])

            with open(row[0], 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_width(image, target_size)
                    cover.save(file_path, image.format)


size = 227
source = '/scratch/liaoi/images'

if len(sys.argv) == 2:
    size = sys.argv[1]

target = 'images_' + str(size)

parent_dir = os.path.dirname(os.path.normpath(source))
target_dir = os.path.join(parent_dir, target)

if not os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.makedirs(target_dir)

resize_file('./train.csv', target_dir, size)
resize_file('./test.csv', target_dir, size)


