import os

folder_path = '/home/enab-muneer/skin_disease_classifier/dark-data/varicella'  # Replace with the actual folder path

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Iterate over each file
for file_name in file_list:
    # Check if it is a file (not a directory)
    if os.path.isfile(os.path.join(folder_path, file_name)):
        # Add the prefix '-d' to the file name
        new_file_name = 'd-' + file_name
        
        # Rename the file
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))