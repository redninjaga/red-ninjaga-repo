# Author: Maksim Derevianko
import os

def change_name(file_name: str) -> str:
    """Replaces first name and last name"""
    full_name, extension = file_name.split('.')
    name, surname = full_name.split('_')
    renamed_file = f"{surname}_{name}.{extension}"
    return renamed_file

path = 'C:/Max/Names'
files = os.listdir(path)

for file in files:
    os.rename(f"{path}/{file}", f"{path}/{change_name(file)}")

