from pathlib import Path
from PIL import Image
from func import *
import os, zipfile, inquirer

src = Path(input('Please insert .cbz: ').strip('& ').strip("'"))
while (str(src) == '.') or (os.path.splitext(src)[1] != '.cbz'):
    src = Path(input('Please insert .cbz: ').strip('& ').strip("'"))

file_name = src.stem

create_temp()

with zipfile.ZipFile(src, 'r') as zip_ref:
    zip_ref.extractall('temp/')

questions = [
    inquirer.List(
        "options",
        message="Desired page width",
        choices=["1200", "1600"],
    ),
]

answers = inquirer.prompt(questions)

resize_width = answers["options"]

def get_ratio():
    h, w = image.size
    
    if w < resize_width:
        print(f"Image width is smaller than {resize_width}, skipping.")
    
    resize_ratio = resize_width / w
    h_new = round(h * resize_ratio)
    return h_new

# Process Images
for i in os.listdir('temp/'):
    if i.endswith('.png') or i.endswith('.jpg'): 
        image = Image.open(f"temp/{i}")
        image = image.resize((get_ratio(), resize_width), resample=Image.Resampling.BICUBIC)
        image.save(f'temp/{i}', optimize = True)
        print(f'{i} proccessed')
        
create_cbz('temp/', 'output/', src.stem)
delete_temp()
print('Rescale has finished.')
pause()