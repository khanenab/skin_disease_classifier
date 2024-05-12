import os

folder_path = '/home/enab-muneer/skin_disease_classifier/mix-data/esantema-iatrogeno-farmaco-indotta'  # Replace with the actual folder path
for filename in os.listdir(folder_path):
    new_filename = filename.replace('-d', '').replace('d-', '')
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))