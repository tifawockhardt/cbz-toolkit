from patoolib import extract_archive
from PIL import Image 
import zipfile, os, fitz, io, shutil, os, sys

# create_cbz(source_folder, output_folder, cbz_filename)
def create_cbz(source_folder, output_folder, cbz_filename):
    cbz_file_path = os.path.join(output_folder, cbz_filename + '.cbz')
    
    with zipfile.ZipFile(cbz_file_path, 'w', zipfile.ZIP_DEFLATED) as cbz_file:
        for foldername, subfolders, filenames in os.walk(source_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, source_folder)
                cbz_file.write(file_path, arcname)

# source_folder = 'path/to/your/source/folder'
# output_folder = 'path/to/your/output'
# cbz_filename = 'output_file'

# pdf_conv(source_file)
def pdf_conv(source_file, output_folder):
    pdf_file = fitz.open(source_file)
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
            image.save(open(f"{output_folder}image_p{format(page_index, '03d')}.{image_ext}", "wb"))
# source_file = 'path/to/your/source/pdf'

# cbr_ex(source_file, output_folder)
def cbr_ex(source_file, output_folder):
    extract_archive(source_file, outdir=output_folder, verbosity=-1)
# source_folder = 'path/to/your/source/cbr'
# output_folder = 'path/to/your/output'

# Create temp folder, check if one exists
def create_temp():
    if os.path.isdir('temp'):
        shutil.rmtree('temp/')
    os.mkdir("temp")
    
def delete_temp():
    shutil.rmtree('temp/')

# Check os and select clear
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# New pause text
def pause():
    os.system('pause')

def delete_last_line(num):
    for n in range(num):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')