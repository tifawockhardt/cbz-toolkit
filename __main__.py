from func import *
from art import *
import os, inquirer

# TODO: 
# Clean up a million things
# Batch
# Phase out Path for os

modules = {"Create": "createcbz", "Convertor": "tocbz", "Add Metadata": "addmetadata", "Downscaler": "resizecomp", "Quit": "quit"}
# , "Renamer": "renamer"

while True: 
    clear()
    if os.path.isdir('temp'):
        shutil.rmtree('temp/')
        
    print(text2art("cbztoolkit"))
    
    questions = [
        inquirer.List(
            "options",
            message="Options",
            choices=["Create", "Convertor", "Metadata", "Downscaler", "Quit"],
        ),
    ]
    # "Renamer",
    
    print('by tifawockhardt\n')

    answers = inquirer.prompt(questions)
    
    clear()
    
    match modules[answers["options"]]: 
        case 'createcbz': import createcbz
            
        case 'tocbz': import tocbz
            
        case 'Metadata': import addmetadata
            
        case 'resizecomp': import resizecomp
        
        # case 'renamer': import renamer
        
        case 'quit':
            clear()
            quit()
    
    pause()