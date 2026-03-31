import matplotlib.pyplot as plt
from nilearn import plotting

def show_slice(data, slice_index):
    plt.imshow(data[:, :, slice_index], cmap='gray')
    plt.title(f"Slice {slice_index}")
    plt.axis('off')
    plt.show()


def plot_brain(img):
    plotting.plot_anat(img)
    plotting.show()

def plot_histogram(data):
    plt.hist(data.flatten(), bins=50)
    plt.title("Voxel Intensity Distribution")
    plt.show()