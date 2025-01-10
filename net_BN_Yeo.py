import pandas as pd
import numpy as np
import os

save_dir = r'\net\net_voxel'

subregion_file = r'\net\subregion_Yeonet.xlsx'
subregion_data = pd.read_excel(subregion_file)

voxel_counts_file = r'\net\brain_area_voxel_counts.xlsx'
voxel_counts_data = pd.read_excel(voxel_counts_file)

merged_data = pd.merge(subregion_data[['Label', 'Yeo_7network']], voxel_counts_data[['region', 'n_voxel']], left_on='Label', right_on='region')

network_voxel_matrix = pd.DataFrame(0, index=range(1, 8), columns=range(1, 247))

for index, row in merged_data.iterrows():
    network = row['Yeo_7network']
    brain_area_index = row['Label']
    voxel_count = row['n_voxel']
    network_voxel_matrix.loc[network, brain_area_index] = voxel_count

print(network_voxel_matrix)

matrix_net_voxel = network_voxel_matrix.values[:7, :]

print(matrix_net_voxel)
print(matrix_net_voxel.shape)
np.save(r'\net\net_voxel.npy', matrix_net_voxel)

file_names = ['VIS.npy', 'SOM.npy', 'DAT.npy', 'VAT.npy', 'LIM.npy', 'FPN.npy', 'DMN.npy']
for i, file_name in enumerate(file_names):
    np.save(os.path.join(save_dir, file_name), matrix_net_voxel[i])

