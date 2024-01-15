from func import create_cbz
import os, sys, subprocess, inquirer, psutil, logging
# import addmetadata, createcbz, resizecomp, tocbz

# TODO: 
# Clean up a million things
# Batch
# Fix find similar
# Fix redundant func input
# Fix tempfile in tocbz
# Print "markers" task done,etc
# Fix Resize names
# Phase out Path for os

modules = {"Create CBZ": "createcbz", "Convert to CBZ": "tocbz", "Add Metadata": "addmetadata", "Downscale CBZ": "resizecomp"}

sys.path.append(os.path.realpath("."))
import inquirer

questions = [
    inquirer.List(
        "options",
        message="What size do you need?",
        choices=["Create CBZ", "Convert to CBZ", "Add Metadata", "Downscale CBZ"],
    ),
]

answers = inquirer.prompt(questions)

print(modules[answers["options"]])