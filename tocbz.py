from pathlib import Path
from PIL import Image 
import os, io, fitz, shutil, patoolib

# Declare root and create temp
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
temp_folder = os.path.join(ROOT_DIR, "temp\\")

src = Path(input('Please insert file: ').strip('& ').strip("'"))
file_name = src.stem

def create_temp():
    new_temp = os.mkdir("temp")

# pdf
def pdf_conv(src):
    pdf_file = fitz.open(src)
    total_pages = len(pdf_file)

    for page_index in range(total_pages):
        page = pdf_file[page_index]
        img_list = page.get_images()
        
        if img_list: 
            print(f"Found {len(img_list)} images on page {page_index}.")
        else:
            print(f"No images found on page {page_index}")
            
        for image_index, img in enumerate(page.get_images(), start=1): 
            xref = img[0] 
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"] 
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(open(f"temp/image_p{format(page_index, '03d')}.{image_ext}", "wb"))

def cbr_conv(src):
    patoolib.extract_archive(src, outdir="temp/")

if str(src).endswith('pdf'):
    create_temp()
    pdf_conv(src)
elif str(src).endswith('cbr'):
    cbr_conv(src)
else:
    print('File format not recognized.')
    os.system('pause')
    exit()
    

# Zip temp
archived = shutil.make_archive(src.stem, 'zip', temp_folder)

newExt = ".cbz"
filePath = Path(file_name).with_suffix(".zip")
filePathNew = filePath.with_suffix(newExt)

try:
    filePath.rename(filePathNew)
    print(f"{filePathNew} has been created.")
except FileNotFoundError:
    print(f"Error: Couldn't find {filePath}.")
except FileExistsError:
    print(f"Error: {filePathNew} already exists.")

# Delete temp
if os.path.isfile(filePathNew):
    shutil.rmtree(temp_folder)