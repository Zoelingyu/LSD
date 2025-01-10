# Import the Leida class
from pyleida import Leida

# Instantiate the Leida class, specifying where our data is located
ld = Leida(r'\data')

# Run the complete pipeline:
# Here, 'TR' specifies the Time Repetition of the fMRI data,
# 'paired_test' specifies whether the groups/conditions are
# independent or related, and 'n_perm' the number of permutations
# that will be used in the statistical analyses.
ld.fit_predict(TR=2, paired_tests=True, n_perm=5_000, save_results=True)

