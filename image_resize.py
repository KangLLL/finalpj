import os
import sys
import shutil
from PIL import Image
from resizeimage import resizeimage
import pandas as pd

def resize_file(csv_file, source_dir, target_dir, target_size):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        file_name = row['FileName']

        file_path = os.path.join(target_dir, file_name)
        source_path = os.path.join(source_dir, file_name)

        with open(source_path, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_width(image, target_size)
                cover.save(file_path, image.format)


size = 227
source = '/scratch/liaoi/images'

if len(sys.argv) == 2:
    size = sys.argv[1]

target = 'images_' + str(size)

source_dir = os.path.normpath(source)
parent_dir = os.path.dirname(source_dir)
target_dir = os.path.join(parent_dir, target)

if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.makedirs(target_dir)

resize_file('./train.csv', source_dir, target_dir, size)
resize_file('./test.csv', source_dir, target_dir, size)


