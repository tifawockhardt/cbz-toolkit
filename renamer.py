from pathlib import Path
from func import *
import os, inquirer
    

info = inquirer.list_input(message="Rename", choices=["Pages", "Folder", "File"])
test = inquirer.confirm(message="Rename")

print(test)
os.system('pause')

def print_reference():
    
    print(
    '''
    Naming scheme:
    Manga Title (Vol/Chap) (Year) (Info) (Group)
    
    Examples:
    One Punch-Man v01 (2014) (Digital) (1r0n)
    Goodbye, Eri (2023)
    One Piece c1060 (2022) (Digital)
    
    
    ''')


clear()
print("\033[1mFILES MUST ALREADY BE NUMERICALLY ORDER\033[0m\n")
print_reference('other')

src = Path(input('Please enter the folder of files to be renamed: ').strip('& ').strip("'"))
while (str(src) == '.'):
    print_reference()
    src = Path(input('Please enter the folder of files to be renamed: ').strip('& ').strip("'"))

def folder():
    clear()
    print("\033[1mFILES MUST ALREADY BE NUMERICALLY ORDERED\033[0m\n")
    print_reference()

    print(src.stem)
    title = inquirer.text(message="Manga title")
    volumes = inquirer.list_input(message="Volumes or Chapters?", choices=["Volumes", "Chapters"])
    delete_last_line(3)
    start = inquirer.text(message="What is the first volume in this folder?")
    year = inquirer.text(message="Release Year")
    digital = inquirer.confirm(message="Is this a digital copy?", default="yes")
    delete_last_line(1)
    group = inquirer.text(message="Release Group (Press Enter if not applicable)")
    print('\n')
    
    if volumes == "Volumes": vce = 'v'
    else: vce = "c"
    if digital: digital = "(Digital)" 
    else: digital = ""
    if group != None: ge = "(" + group + ")"
    else: ge = ""
    if year != None: ye = "(" + year + ")"
    else: ye = ""

    clear()
    print("\033[1mFILES MUST ALREADY BE NUMERICALLY ORDERED\033[0m\n")
    print_reference()

    print(f'{title} {vce}{start} {ye} {digital} {ge}')
    confirm = inquirer.confirm(message="Does this information look correct?", default="yes")
    return [title, volumes, start, year, digital, group, confirm]

def file():
    clear()
    print_reference()

    print(src.stem)
    title = inquirer.text(message="Manga title")
    series = inquirer.list_input(message="Is this a series or one-shot?", choices=["Series", "One-Shot"])
    volumes = inquirer.list_input(message="Volumes or Chapters?", choices=["Volumes", "Chapters"])
    delete_last_line(3)
    if series == 'Series':
        num = inquirer.text(message="Which volume/chapter is this?", choices=["Volumes", "Chapters"])
    year = inquirer.text(message="Release Year")
    digital = inquirer.confirm(message="Is this a digital copy?", default="yes")
    delete_last_line(1)
    group = inquirer.text(message="Release Group (Press Enter if not applicable)")
    print('\n')
    
    if volumes == "Volumes": vce = 'v'
    else: vce = "c"
    if digital: digital = "(Digital)" 
    else: digital = ""
    if group != None: ge = "(" + group + ")"
    else: ge = ""
    if year != None: ye = "(" + year + ")"
    else: ye = ""

    clear()
    print("\033[1mFILES MUST ALREADY BE NUMERICALLY ORDERED\033[0m\n")
    print_reference()

    print(f'{title} {vce}{num} {ye} {digital} {ge}')
    confirm = inquirer.confirm(message="Does this information look correct?", default="yes")
    return [title, series, volumes, num, year, digital, group, confirm]

match info: 
    case 'Folder':
        folder_info = folder()
        
        # Renaming

    case 'File':
        file_info = file()
        

# for i in os.listdir(src):
    




pause()