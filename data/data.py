from nilearn import datasets

from nilearn.image import resample_to_img

img1 = datasets.load_mni152_template()

img2 = datasets.load_mni152_gm_template()

# Check shapes
print(img1.shape, img2.shape)


img2_resampled = resample_to_img(img2, img1)
data1 = img1.get_fdata()
data2 = img2_resampled.get_fdata()