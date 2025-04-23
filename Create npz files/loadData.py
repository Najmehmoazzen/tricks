import numpy as np
# load data forward.npz
scale_factor = 100  
loaded = np.load(f'./result.npz')
array_loaded_total=loaded['data'].astype(np.float32) / scale_factor
print(array_loaded_total.shape)
print(array_loaded_total[0,0])
print(array_loaded_total[1,1])
print(array_loaded_total[30000,0])
print(array_loaded_total[30000,1])