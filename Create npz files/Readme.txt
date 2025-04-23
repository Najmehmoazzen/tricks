# load data forward.npz
scale_factor = 100  
loaded = np.load('./Forward.npz')
array_loaded_total=loaded['result'].astype(np.float32) / scale_factor