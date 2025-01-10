import nibabel as nib
import numpy as np
import pandas as pd

path_data = r'C:\Users\hbhwl\Desktop\Ketamine_MDD\Brainnetome_Atlas\BN_Atlas_246_2mm.nii'

img = nib.load(path_data)
data = img.get_fdata()

unique_values, counts = np.unique(data, return_counts=True)

result_df = pd.DataFrame(columns=["脑区", "体素数量"])

for value, count in zip(unique_values, counts):
    result_df = pd.concat([result_df, pd.DataFrame({"脑区": [int(value)], "体素数量": [count]})], ignore_index=True)

result_df.to_csv(r'C:/Users/hbhwl/Desktop/Ketamine_MDD/Brainnetome_Atlas/brain_area_voxel_counts.csv', index=False)

result_df.to_excel(r'C:/Users/hbhwl/Desktop/Ketamine_MDD/Brainnetome_Atlas/brain_area_voxel_counts.xlsx', index=False)


