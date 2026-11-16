

import random

# OS CA-2: Page Replacement Performance Investigation
# Algorithms: FIFO, LRU and Optimal


# FIFO Algorithm
def fifo(pages, frames):
    memory = []
    faults = 0
    hits = 0
    pointer = 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames

    return faults, hits


# LRU Algorithm
def lru(pages, frames):
    memory = []
    faults = 0
    hits = 0

    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

    return faults, hits


# Optimal Algorithm
def optimal(pages, frames):
    memory = []
    faults = 0
    hits = 0

    for i, page in enumerate(pages):
        if page in memory:
            hits += 1
        else:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i + 1:]
                distances = []

                for item in memory:
                    if item in future:
                        distances.append(future.index(item))
                    else:
                        distances.append(float('inf'))

                replace_index = distances.index(max(distances))
                memory[replace_index] = page

    return faults, hits


# Algorithm List
algorithms = [
    ("FIFO", fifo),
    ("LRU", lru),
    ("Optimal", optimal)
]


# Main Page Reference String
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

print("=" * 70)
print("       OS PERFORMANCE INVESTIGATION")
print("       PAGE REPLACEMENT ALGORITHMS")
print("=" * 70)

print("\nPage Reference String:", pages)
print("Total Page References:", len(pages))


# Experiment 1: Algorithm Comparison Using 3 Frames
print("\nEXPERIMENT 1: ALGORITHM COMPARISON")
print("-" * 70)

frames = 3

print("Number of Frames:", frames)
print(f"{'Algorithm':<15}{'Faults':<12}{'Hits':<12}"
      f"{'Hit Ratio':<12}{'Fault Rate':<12}")

for name, algorithm in algorithms:
    faults, hits = algorithm(pages, frames)

    hit_ratio = hits / len(pages)
    fault_rate = faults / len(pages)

    print(f"{name:<15}{faults:<12}{hits:<12}"
          f"{hit_ratio:<12.3f}{fault_rate:<12.3f}")


# Experiment 2: Different Frame Sizes
print("\n\nEXPERIMENT 2: PERFORMANCE WITH DIFFERENT FRAME SIZES")
print("-" * 70)

for frames in [2, 3, 4, 5]:
    print(f"\nNumber of Frames: {frames}")
    print(f"{'Algorithm':<15}{'Faults':<12}{'Hits':<12}"
          f"{'Hit Ratio':<12}{'Fault Rate':<12}")

    for name, algorithm in algorithms:
        faults, hits = algorithm(pages, frames)

        hit_ratio = hits / len(pages)
        fault_rate = faults / len(pages)

        print(f"{name:<15}{faults:<12}{hits:<12}"
              f"{hit_ratio:<12.3f}{fault_rate:<12.3f}")


# Experiment 3: Belady's Anomaly in FIFO
print("\n\nEXPERIMENT 3: BELADY'S ANOMALY")
print("-" * 70)

belady_pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

print("Reference String:", belady_pages)
print("\nFIFO Page Fault Comparison:")

for frames in [3, 4]:
    faults, hits = fifo(belady_pages, frames)

    print(f"Frames: {frames} | Page Faults: {faults} | Page Hits: {hits}")


# Experiment 4: Different Page Reference Workloads
print("\n\nEXPERIMENT 4: DIFFERENT WORKLOAD PATTERNS")
print("-" * 70)

# Workload 1: Locality of Reference
locality_pages = [
    1, 2, 3, 1, 2, 3, 4, 1,
    2, 3, 4, 5, 1, 2, 3, 4,
    5, 1, 2, 3, 1, 2, 3, 4
]

# Workload 2: Random Access
# Fixed seed ensures repeatable results
random_generator = random.Random(42)
random_pages = random_generator.choices(range(1, 9), k=24)

# Workload 3: Sequential Access
sequential_pages = list(range(1, 13)) * 2

workloads = [
    ("Locality", locality_pages),
    ("Random", random_pages),
    ("Sequential", sequential_pages)
]

frames = 3

for workload_name, workload_pages in workloads:

    print(f"\nWorkload: {workload_name}")
    print("Reference String:", workload_pages)

    print(f"{'Algorithm':<15}{'Faults':<12}{'Hits':<12}"
          f"{'Hit Ratio':<12}{'Fault Rate':<12}")

    for name, algorithm in algorithms:
        faults, hits = algorithm(workload_pages, frames)

        hit_ratio = hits / len(workload_pages)
        fault_rate = faults / len(workload_pages)

        print(f"{name:<15}{faults:<12}{hits:<12}"
              f"{hit_ratio:<12.3f}{fault_rate:<12.3f}")


# Experiment Completed
print("\n" + "=" * 70)
print("          ALL EXPERIMENTS COMPLETED")
print("=" * 70)
