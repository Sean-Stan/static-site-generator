import os
import shutil


def copy_source_to_destination(source_path, destination_path):
    if (not os.path.exists(source_path) or not os.path.exists(destination_path)):
        return

    if os.path.isfile(source_path):
        shutil.copy(source_path, destination_path)
        return
    
    shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    
    files = os.listdir(source_path)

    for file in files:
        old_file_or_folder = os.path.join(source_path, file)
        if os.path.isfile(old_file_or_folder):
            dest_file_path = os.path.join(destination_path, file)
            shutil.copy(old_file_or_folder, dest_file_path)
        else:
            new_folder = os.path.join(destination_path, file)
            os.mkdir(new_folder)
            copy_source_to_destination(old_file_or_folder, new_folder)