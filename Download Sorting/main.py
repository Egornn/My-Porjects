import os
import shutil

downloads_folder = 'C:\Users\Егор\Downloads'

file_types = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.flac', '.ogg']
}

for folder in file_types.keys():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        file_category = None
        for category, extensions in file_types.items():
            if file_extension in extensions:
                file_category = category
                break

        if file_category:
            destination_folder = os.path.join(downloads_folder, file_category)
            shutil.move(file_path, destination_folder)
            print(f"Moved {filename} to {file_category} folder.")
        else:
            print(f"Skipping {filename}: Unknown file type.")

print("File organization complete.")
