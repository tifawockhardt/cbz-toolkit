from pathlib import Path
import os
from func import *

src = Path(input('Please insert .cbz: ').strip('& ').strip("'"))
while (str(src) == '.') or (os.path.splitext(src)[1] != '.cbz'):
    src = Path(input('Please insert .cbz: ').strip('& ').strip("'"))
    
file_name, file_ext = os.path.splitext(src)

create_temp()

match file_ext:
    case '.pdf':
        pdf_conv(src, 'temp/')
        create_cbz('temp/', 'output/', src)
    case '.cbr':
        cbr_ex(src, 'temp/')
        create_cbz('temp/', 'output/', src)
    case '.zip':
        src.rename(src.with_suffix('.cbz'))
    case _: 
        print('File format not recognized.')
        exit()

if os.path.isfile(src):
    delete_temp()
    
print('File has been converted.')
pause()