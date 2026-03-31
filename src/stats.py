import numpy as np
import matplotlib.pyplot as plt

def compute_basic_stats(data):
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data)
    }

def plot_histogram(data):
    plt.hist(data.flatten(), bins=50)
    plt.title("Voxel Intensity Distribution")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.show()