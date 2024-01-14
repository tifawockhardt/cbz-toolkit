from PIL import Image
from pathlib import Path
import shutil, os

src = Path(input('Please insert file: ').strip('& ').strip("'"))
file_name = src.stem
output = 'output/'

archived = shutil.make_archive(file_name, 'zip', src)

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
    
src_move = shutil.move(filePathNew, 'output/')
