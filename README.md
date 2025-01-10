LEiDA_run.py: This script uses the Leida package to extract k metastable states and calculates the probability of occurrence, dwell time, and state transition matrix. The code is based on the reference from https://github.com/PSYMARKER/leida-python.

OP_calculated.py: This script calculates the Kuramoto Order Parameter (OP) for each subject and computes the average OP and the standard deviation of OP (i.e., STD(OP)) for each condition.

CBIG_pFIC.py: This script simulates the E/I ratio. The input file for this script is parse.ini. The code is based on the reference from https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/fMRI_dynamics/Zhang2024_pFIC.

brain_area_voxel_counts.py and net_BN_Yeo.py: These scripts extract the seven resting-state networks vectors from the Yeo atlas to calculate the spatial overlap with each PL State. The approach is based on the reference from https://github.com/juanitacabral/LEiDA_Psilocybin/blob/master/OverlapYeo.m.
