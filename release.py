import os
import shutil

source_folder = input("Enter the source folder path: ")

destination_folder = input("Enter the destination folder path: ")

for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)

    if os.path.isfile(source_file):
        file_name, file_extension = os.path.splitext(filename)
        
        target_folder = os.path.join(destination_folder, file_name)
        os.makedirs(target_folder, exist_ok=True)
        
        shutil.move(source_file, os.path.join(target_folder, filename))

print('Operation completed.')
