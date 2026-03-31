import matplotlib.pyplot as plt
from nilearn import plotting
import numpy as np


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

def browse_slices(data):
    num_slices = data.shape[2]
    slice_index = num_slices // 2  # start in the middle

    fig, ax = plt.subplots()

    # Initial slice
    slice_data = data[:, :, slice_index]
    vmin, vmax = np.percentile(slice_data, (1, 99))

    img_plot = ax.imshow(slice_data, cmap='gray', vmin=vmin, vmax=vmax)
    ax.set_title(f"Slice {slice_index}")
    plt.axis('off')

    def on_key(event):
        nonlocal slice_index

        if event.key == 'right':
            slice_index = (slice_index + 1) % num_slices
        elif event.key == 'left':
            slice_index = (slice_index - 1) % num_slices

        # Update slice FIRST
        slice_data = data[:, :, slice_index]

        # THEN compute contrast
        vmin, vmax = np.percentile(slice_data, (1, 99))

        img_plot.set_data(slice_data)
        img_plot.set_clim(vmin, vmax)

        ax.set_title(f"Slice {slice_index}")
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

