import numpy as np
import os
import re
def list_files(directory):
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        files = [f for f in files if f.endswith('.npz')]
        return files
    except Exception as e:
        return str(e)
def extract_coupling(file_name):
    match = re.search(r'copling=([0-9.]+)', file_name)
    return float(match.group(1)) if match else float('inf')

directory_path='./B/'
files = list_files(directory_path)
files = sorted(files, key=extract_coupling)
print(files)
directory_path='./B/'
directory_path_output='./B_new/'
os.makedirs(directory_path_output, exist_ok=True)
print('📂 Create folders for saving data.')
for file in files:# Loop through all files in the list (assuming 'files' is defined earlier)
    file_path = directory_path + file  # Construct the full file path (without .txt yet)
    try:        
        loaded = np.load(file_path)
        array_loaded=loaded['phases']
        new_array = array_loaded[:, 4:1000:10]
        np.savez_compressed(directory_path_output + file, phases=new_array)        # Save the processed 2D array in compressed format
    except Exception as e:
        print("❌ Error reading the file:", e)        # Print error message if file reading or processing fails
    print(file+str(new_array.shape)+'Saved.')# Print the final shape of the last processed dataset
