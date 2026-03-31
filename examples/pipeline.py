import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from nilearn import datasets
from visualization import plot_brain, show_slice, browse_slices
from stats import compute_basic_stats

# Load sample brain
img = datasets.load_mni152_template()
data = img.get_fdata()

# 1. Show middle slice
middle_slice = data.shape[2] // 2
show_slice(data, middle_slice)

# 2. Show full brain
plot_brain(img)

browse_slices(data)

# 3. Compute stats
stats = compute_basic_stats(data)
print("Voxel stats:", stats)