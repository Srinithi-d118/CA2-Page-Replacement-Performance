

import os
import tempfile
import shutil
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Temporary folder for generating graphs
temp_folder = tempfile.gettempdir()


# Function to save graphs without overwriting existing files
def save_graph(filename):
    temp_path = os.path.join(temp_folder, filename)
    final_path = os.path.join("graphs", filename)

    plt.savefig(temp_path, dpi=300, bbox_inches="tight")
    plt.close()

    if os.path.exists(final_path):
        print(filename, "already exists. Keeping original file.")
    else:
        shutil.copy2(temp_path, final_path)
        print(filename, "saved successfully.")


# --------------------------------------------------
# EXPERIMENT 1: Algorithm Comparison
# --------------------------------------------------

algorithms = ["FIFO", "LRU", "Optimal"]
faults = [10, 9, 7]

plt.figure(figsize=(8, 5))
plt.bar(algorithms, faults)

plt.title("Page Fault Comparison of Replacement Algorithms")
plt.xlabel("Page Replacement Algorithms")
plt.ylabel("Number of Page Faults")

plt.tight_layout()

save_graph("graph1_algorithm_comparison.png")


# --------------------------------------------------
# EXPERIMENT 2: Different Frame Sizes
# --------------------------------------------------

frames = [2, 3, 4, 5]

fifo_faults = [11, 10, 7, 6]
lru_faults = [11, 9, 6, 6]
optimal_faults = [9, 7, 6, 6]

plt.figure(figsize=(8, 5))

plt.plot(frames, fifo_faults, marker="o", label="FIFO")
plt.plot(frames, lru_faults, marker="s", label="LRU")
plt.plot(frames, optimal_faults, marker="^", label="Optimal")

plt.title("Page Faults vs Number of Memory Frames")
plt.xlabel("Number of Memory Frames")
plt.ylabel("Number of Page Faults")

plt.xticks(frames)
plt.legend()
plt.grid(True)
plt.tight_layout()

save_graph("graph2_frame_comparison.png")


# --------------------------------------------------
# EXPERIMENT 3: Belady's Anomaly
# --------------------------------------------------

belady_frames = [3, 4]
belady_faults = [9, 10]

plt.figure(figsize=(8, 5))

plt.plot(belady_frames, belady_faults, marker="o")

plt.title("Belady's Anomaly in FIFO Algorithm")
plt.xlabel("Number of Memory Frames")
plt.ylabel("Number of Page Faults")

plt.xticks(belady_frames)
plt.grid(True)
plt.tight_layout()

save_graph("graph3_beladys_anomaly.png")


# --------------------------------------------------
# EXPERIMENT 4: Workload Comparison
# --------------------------------------------------

workloads = ["Locality", "Random", "Sequential"]

fifo_workload = [18, 19, 24]
lru_workload = [18, 17, 24]
optimal_workload = [11, 12, 21]

x = range(len(workloads))
width = 0.25

plt.figure(figsize=(9, 5))

plt.bar(
    [i - width for i in x],
    fifo_workload,
    width,
    label="FIFO"
)

plt.bar(
    x,
    lru_workload,
    width,
    label="LRU"
)

plt.bar(
    [i + width for i in x],
    optimal_workload,
    width,
    label="Optimal"
)

plt.title("Page Fault Comparison Across Workloads")
plt.xlabel("Workload Patterns")
plt.ylabel("Number of Page Faults")

plt.xticks(list(x), workloads)
plt.legend()
plt.tight_layout()

save_graph("graph4_workload_comparison.png")


# --------------------------------------------------
# COMPLETION MESSAGE
# --------------------------------------------------

print("\n" + "=" * 55)
print("GRAPH GENERATION PROCESS COMPLETED")
print("=" * 55)

print("\nCheck the graphs folder for the generated files.")
