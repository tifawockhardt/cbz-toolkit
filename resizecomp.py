from pathlib import Path
from PIL import Image
import os, io, fitz, shutil, patoolib, zipfile, sys
from func import *


# filepath = Path('temp/One-Punch Man - c122 (v25) - p102 [VIZ Media] [Digital] [1r0n].png')

src = Path(input('Please insert file: ').strip('& ').strip("'"))
file_name = src.stem

create_temp()

with zipfile.ZipFile(src, 'r') as zip_ref:
    zip_ref.extractall('temp/')

resize_width = 1600

def get_ratio():
    h, w = image.size
    
    if w < resize_width:
        print(f"Image width is smaller than {resize_width}, skipping.")
    
    resize_ratio = resize_width / w
    h_new = round(h * resize_ratio)
    return h_new

for i in os.listdir('temp/'):
    if i.endswith('.png') or i.endswith('.jpg'): 
        image = Image.open(f"temp/{i}")
        image = image.resize((get_ratio(), resize_width), resample=Image.Resampling.BICUBIC)
        image.save(f'temp/{i}', optimize = True)
        print(f'{i} proccessed')
        
create_cbz('temp/', 'output/', src.stem)

# Delete temp
if os.path.isfile(src):
    delete_temp()