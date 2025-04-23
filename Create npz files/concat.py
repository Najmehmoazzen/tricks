import numpy as np
import os
import re
#from tqdm import tqdm  # for progress bar

Forward_or_Backward = "B"
directory_path = f'./{Forward_or_Backward}/'

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

files = list_files(directory_path)
files = sorted(files, key=extract_coupling)

# Calculate total shape (we assume all files have same number of columns)
total_rows = 0
n_cols = None
file_shapes = []

i=1
n_files=len(files)
for file_name in files:
    print(f"Scanning files: {i}/{n_files}")
    data = np.load(os.path.join(directory_path, file_name))['phases']
    rows, cols = data.shape
    file_shapes.append(rows)
    total_rows += rows
    if n_cols is None:
        n_cols = cols
    i+=1

# Path to the .dat file for memmap storage
memmap_file = os.path.join(directory_path, 'result.dat')

# Create memory-mapped file on disk with the total shape
final_array = np.memmap(memmap_file, dtype='float64', mode='w+', shape=(total_rows, n_cols))
print("✅ Create memory-mapped file")

# Fill the memmap array incrementally
start_row = 0
i=1
for file_name in files:
    print(f"Scanning files: {i}/{n_files}")
    file_path = os.path.join(directory_path, file_name)
    data = np.load(file_path)['phases']
    end_row = start_row + data.shape[0]
    final_array[start_row:end_row, :] = data
    start_row = end_row
    i+=1
print("✅ Fill the memmap array incrementally")


# Flush changes to disk
final_array.flush()
print("✅ Flush changes to disk")

# Save to compressed .npz file
np.savez_compressed(os.path.join(directory_path, 'result.npz'), data=final_array)

print("✅ Save to compressed .npz file")

print(f"\n✅ Finished! Final shape: {final_array.shape}")
print(f"📁 Saved compressed file as: result.npz")
