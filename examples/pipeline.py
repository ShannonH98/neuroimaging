import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from stats import plot_histogram
from nilearn import datasets
import nibabel as nib
from visualization import plot_brain, show_slice, browse_slices
from stats import advanced_stats, threshold,compare_images
import matplotlib.pyplot as plt
from nilearn.image import resample_to_img

# Load sample brain
img = datasets.load_mni152_template()
data = img.get_fdata()

#Visualization
middle_slice = data.shape[2] // 2
show_slice(data, middle_slice)

plot_brain(img)

browse_slices(data)

# 3. Compute stats
stats = advanced_stats(data)
print("Voxel stats:", stats)

plot_histogram(data)


img1 = datasets.load_mni152_template()      # template brain
img2 = datasets.load_mni152_gm_template()   # gray matter template (slightly different)


img2_resampled = resample_to_img(img2, img1)

data1 = img1.get_fdata()
data2 = img2_resampled.get_fdata()


stats, diff = compare_images(data1, data2)

print(stats)