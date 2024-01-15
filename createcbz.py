from pathlib import Path
from func import *
import os

src = Path(input('Please insert path: ').strip('& ').strip("'"))
while (str(src) == '.'):
    src = Path(input('Please insert path: ').strip('& ').strip("'"))

file_name = src
output = 'output/'

create_cbz(src, 'output/', src.stem)
print("File has been created.")
pause()