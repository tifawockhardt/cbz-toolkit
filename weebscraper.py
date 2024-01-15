from func import *
from art import *
import os, sys, inquirer

# TODO: 
# Clean up a million things
# Batch
# Fix find similar
# Fix redundant func input
# Fix tempfile in tocbz
# Print "markers" task done,etc
# Fix Resize names
# Phase out Path for os

modules = {"Create CBZ": "createcbz", "Convert to CBZ": "tocbz", "Add Metadata": "addmetadata", "Downscale CBZ": "resizecomp", "Quit": "quit"}

# sys.path.append(os.path.realpath("."))
while True: 
    clear()
    
    Art=text2art("cbztoolkit") # random font mode
    print(Art)
    
    questions = [
        inquirer.List(
            "options",
            message="Options",
            choices=["Create CBZ", "Convert to CBZ", "Add Metadata", "Downscale CBZ", "Quit"],
        ),
    ]

    answers = inquirer.prompt(questions)
    
    match modules[answers["options"]]: 
        case 'createcbz': import test
            
        case 'tocbz': import tocbz
            
        case 'addmetadata': import addmetadata
            
        case 'resizecomp': import resizecomp
        
        case 'quit':
            clear()
            quit()
    pause()