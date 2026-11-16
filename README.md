# CA2 – Performance Investigation
## Page Replacement Algorithms

### Project Overview
This project investigates and compares different page replacement algorithms used in Operating Systems.

### Algorithms Implemented
1. FIFO (First In First Out)
2. LRU (Least Recently Used)
3. Optimal Page Replacement

### Experiments
- FIFO Page Replacement
- LRU Page Replacement
- Optimal Page Replacement
- Page Replacement Algorithm Comparison
- Thrashing Simulation

### Technologies Used
- Python 3
- Ubuntu Linux
- Visual Studio Code

### Performance Analysis
The algorithms are compared based on:
- Page faults
- Page hits
- Number of frames
- Performance under different reference strings

### Comparison Results
For the reference string `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]` with 3 frames:

| Algorithm | Page Faults | Page Hits |
|---|---:|---:|
| FIFO | 10 | 3 |
| LRU | 9 | 4 |
| Optimal | 7 | 6 |

### Conclusion
This investigation demonstrates how different page replacement algorithms affect memory performance. Optimal produced the fewest page faults in the tested reference string.