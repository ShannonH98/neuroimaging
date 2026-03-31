from src.loader import load_nifti
from src.visualization import show_slice
from src.stats import compute_basic_stats

img, data = load_nifti("data/sample.nii")

show_slice(data, slice_index=50)

stats = compute_basic_stats(data)
print(stats)