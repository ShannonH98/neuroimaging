import numpy as np
import matplotlib.pyplot as plt

def advanced_stats(data):
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "p95": np.percentile(data, 95),
        "non_zero_voxels": np.count_nonzero(data)
    }

def plot_histogram(data):
    plt.hist(data.flatten(), bins=50)
    plt.title("Voxel Intensity Distribution")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.show()

def threshold(data, threshold_value):
    return np.where(data > threshold_value, data, 0)


def compare_images(data1, data2, visualize=True):
    diff = np.abs(data1 - data2)

    stats = {
        "mean_diff": np.mean(diff),
        "std_diff": np.std(diff),
        "max_diff": np.max(diff),
        "nonzero_voxels": np.count_nonzero(diff),
    }

    if visualize:
        num_slices = diff.shape[2]
        slice_index = num_slices // 2
        fig, ax = plt.subplots()

        img_plot = ax.imshow(diff[:, :, slice_index], cmap='hot')
        ax.set_title(f"Diff Slice {slice_index}")
        plt.axis('off')

        def on_key(event):
            nonlocal slice_index
            if event.key == 'right':
                slice_index = (slice_index + 1) % num_slices
            elif event.key == 'left':
                slice_index = (slice_index - 1) % num_slices

            slice_data = diff[:, :, slice_index]
            img_plot.set_data(slice_data)
            img_plot.set_clim(slice_data.min(), slice_data.max())
            ax.set_title(f"Diff Slice {slice_index}")
            fig.canvas.draw_idle()

        fig.canvas.mpl_connect('key_press_event', on_key)
        plt.show()

    return stats, diff