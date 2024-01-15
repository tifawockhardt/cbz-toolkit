from PIL import Image
from pathlib import Path
from func import create_cbz
import shutil, os

src = Path(input('Please insert file: ').strip('& ').strip("'"))
file_name = src.stem
output = 'output/'

create_cbz(src, 'output/', src.stem)