import os
import numpy as np
import pandas as pd
from scipy.signal import hilbert
from scipy.stats import ttest_rel

lsd_dir = r' '
plcb_dir = r' '
output_csv = r'\OP.csv'

lsd_output_dir = r' '
plcb_output_dir = r' '
average_output_dir = r' '

os.makedirs(lsd_output_dir, exist_ok=True)
os.makedirs(plcb_output_dir, exist_ok=True)

results = []


def calculate_order_parameter(X):
    phases = np.angle(hilbert(X, axis=1))
    N, T = X.shape
    r = np.zeros(T)

    for t in range(T):
        current_phases = phases[:, t]
        z = np.exp(1j * current_phases)
        r[t] = np.abs(np.sum(z)) / N

    return r


for file in os.listdir(lsd_dir):
    if file.endswith('.npy'):
        subject_id = file.split('_')[1].split('.')[0]
        file_path = os.path.join(lsd_dir, file)
        X_lsd = np.load(file_path)
        order_parameter_lsd = calculate_order_parameter(X_lsd)

        np.save(os.path.join(lsd_output_dir, f'lsd01_{subject_id}.npy'), order_parameter_lsd)

        mean_r_lsd = np.mean(order_parameter_lsd)
        std_r_lsd = np.std(order_parameter_lsd)
        results.append([subject_id, 'LSD', mean_r_lsd, std_r_lsd])

for file in os.listdir(plcb_dir):
    if file.endswith('.npy'):
        subject_id = file.split('_')[1].split('.')[0]
        file_path = os.path.join(plcb_dir, file)
        X_plcb = np.load(file_path)
        order_parameter_plcb = calculate_order_parameter(X_plcb)

        np.save(os.path.join(plcb_output_dir, f'plcb01_{subject_id}.npy'), order_parameter_plcb)

        mean_r_plcb = np.mean(order_parameter_plcb)
        std_r_plcb = np.std(order_parameter_plcb)
        results.append([subject_id, 'PLCB', mean_r_plcb, std_r_plcb])

df = pd.DataFrame(results, columns=['Subject ID', 'Condition', 'Mean Order Parameter', 'STD Order Parameter'])

mean_r_lsd = df[df['Condition'] == 'LSD']['Mean Order Parameter'].to_numpy()
std_r_lsd = df[df['Condition'] == 'LSD']['STD Order Parameter'].to_numpy()

mean_r_plcb = df[df['Condition'] == 'PLCB']['Mean Order Parameter'].to_numpy()
std_r_plcb = df[df['Condition'] == 'PLCB']['STD Order Parameter'].to_numpy()

if len(mean_r_lsd) == len(mean_r_plcb):
    t_test_r = ttest_rel(mean_r_lsd, mean_r_plcb)
    t_test_std_r = ttest_rel(std_r_lsd, std_r_plcb)

    print(f'T-test for Kuramoto Order Parameter: t-statistic = {t_test_r.statistic}, p-value = {t_test_r.pvalue}')
    print(
        f'T-test for Standard Deviation of Order Parameter: t-statistic = {t_test_std_r.statistic}, p-value = {t_test_std_r.pvalue}')
else:
    print("Error: The number of subjects in LSD and PLCB conditions do not match.")


df.to_csv(output_csv, index=False)

np.save(os.path.join(average_output_dir, 'OP_average_lsd.npy'), mean_r_lsd)
np.save(os.path.join(average_output_dir, 'OP_average_plcb.npy'), mean_r_plcb)
np.save(os.path.join(average_output_dir, 'OPSTD_average_lsd.npy'), std_r_lsd)
np.save(os.path.join(average_output_dir, 'OPSTD_average_plcb.npy'), std_r_plcb)

print("saved")