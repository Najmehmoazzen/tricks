
import numpy as np
import os
import re

# ------------------------------ Load and Analyze Data ------------------------------
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

# ------------------------------ Configuration ------------------------------

directory_path = './B_new/'
files = list_files(directory_path)
files = sorted(files, key=extract_coupling)
print(files)

all_phases = np.empty((0, 100), dtype=np.float32)  # Assuming fixed 100 columns
for file in files:
    loaded = np.load(os.path.join(directory_path, file))
    phases = loaded['phases']
    all_phases = np.vstack((all_phases, phases))
    print(file)

np.savez_compressed(f'Big_Data.npz', result=all_phases)
print(f"✅ Saved compressed file: Big_Data.npz | Shape: {all_phases.shape}")

# load data forward.npz
# Load the compressed .npz file and rescale to float32
#scale_factor = 100
#loaded = np.load(f'./{Forward_or_Backward}.npz')
#phases_loaded = loaded['result'].astype(np.float32) / scale_factor
#print(f"✅ Loaded data shape: {phases_loaded.shape}")

