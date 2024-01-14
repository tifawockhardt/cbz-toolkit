from pathlib import Path
from PIL import Image
import os, io, fitz, shutil, patoolib, zipfile


# filepath = Path('temp/One-Punch Man - c122 (v25) - p102 [VIZ Media] [Digital] [1r0n].png')

# dir = Path('temp/')

src = Path(input('Please insert file: ').strip('& ').strip("'"))
file_name = src.stem

os.mkdir("temp")

with zipfile.ZipFile(src, 'r') as zip_ref:
    zip_ref.extractall('temp/')

dir = os.listdir('temp/')

resize_width = 1600
# image = Image.open(filepath)
# image_name = filepath.stem
# print(image.size)

def get_ratio():
    h, w = image.size
    
    if w < resize_width:
        print(f"Image width is smaller than {resize_width}, skipping.")
        return
    
    resize_ratio = resize_width / w
    h_new = round(h * resize_ratio)
    return h_new


for i in os.listdir('temp/'):
    if i.endswith('.png') or i.endswith('.jpg'): 
        image = Image.open(f"temp/{i}")
        image = image.resize((get_ratio(), resize_width), resample=Image.Resampling.BICUBIC)
        image.save(f'temp/{i}', optimize = True)
        print(f'{i} proccessed')
        
archived = shutil.make_archive(file_name, 'zip', 'temp/')

newExt = ".cbz"
filePath = Path(file_name).with_suffix(".zip")
filePathNew = filePath.with_suffix(newExt)
filePathResize = Path((f'{file_name} (x{resize_width})')).with_suffix(newExt)

try:
    filePath.rename(filePathResize)
    print(f"{filePathNew} has been created.")
except FileNotFoundError:
    print(f"Error: Couldn't find {filePath}.")
except FileExistsError:
    print(f"Error: {filePathNew} already exists.")

# Delete temp
if os.path.isfile(filePathResize):
    shutil.rmtree('temp/')