# from src.helpers import utils, datasets
# train_loader = datasets.get_dataloaders('openimages',
#                                         root=r'C:\Users\james\research\high-fidelity-generative-compression\data\openimages',
#                                         batch_size=2,
#                                         logger=3,
#                                         mode='train',
#                                         shuffle=True)


# import h5py
# import numpy as np
# import pandas as pd
# FILENAME = r'C:\Users\james\research\high-fidelity-generative-compression\reconstructions\compression_metrics.h5'
# b = pd.read_hdf(FILENAME)
# with h5py.File(FILENAME, 'r') as hdf:
#     items = list(hdf.items())
#     print(items)
#     g1 = hdf.get('df')
#     g1items = list(g1.items())
#     axis1 = np.array(g1.get('axis1'))
#     print(axis1)
import pickle
filename = 'stored.pkl'
with open(filename, 'rb') as f:
    x = pickle.load
    print(type(x))