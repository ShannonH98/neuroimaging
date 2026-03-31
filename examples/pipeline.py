import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from stats import plot_histogram
from nilearn import datasets
from visualization import plot_brain, show_slice, browse_slices
from stats import compute_basic_stats

# Load sample brain
img = datasets.load_mni152_template()
data = img.get_fdata()

#Visualization
middle_slice = data.shape[2] // 2
show_slice(data, middle_slice)

plot_brain(img)

browse_slices(data)

# 3. Compute stats
stats = compute_basic_stats(data)
print("Voxel stats:", stats)

plot_histogram(data)