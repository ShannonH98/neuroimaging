import nibabel as nib

def load_nifti(file_path):
    img = nib.load(file_path)
    data = img.get_fdata()
    return img, data