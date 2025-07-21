# Assignment 3: Algorithm Efficiency and Scalability

## Overview

This repository contains implementations and analysis of two key algorithmic concepts:

- **Randomized Quicksort** (with comparison to Deterministic Quicksort)
- **Hash Table with Chaining**

All code is implemented in Python.

---

## Files

- `assignment3_algorithms.py`: Python source code containing:
  - Randomized Quicksort
  - Deterministic Quicksort
  - Hash Table using Chaining
  - Performance comparison tests and results logging

---

## Running the Code

Ensure Python 3 is installed. To execute the program:

```bash
python3 assignment3_algorithms.py
```

This will:

1. Execute Randomized Quicksort and Deterministic Quicksort on multiple datasets:
   - Random Arrays
   - Sorted Arrays
   - Reverse Sorted Arrays
   - Arrays with Repeated Elements

2. Display execution times and handle failure cases (e.g., recursion depth errors in Deterministic Quicksort).

3. Demonstrate hash table operations including:
   - Insert
   - Search
   - Delete

4. Print the internal state of the hash table after operations.

---

## Summary of Findings

- **Randomized Quicksort** demonstrated consistent O(n log n) performance across all datasets, successfully handling large input sizes.
- **Deterministic Quicksort** performed efficiently only on random datasets but failed or severely slowed on sorted/reverse-sorted inputs due to unbalanced partitions, confirming its O(n²) worst-case behavior.
- The **Hash Table with Chaining** supported efficient insert, search, and delete operations. Theoretical average complexity remained O(1 + alpha), where alpha is the load factor. Recommendations for maintaining performance through dynamic resizing are discussed in the report.

---

## References

- Ali, I., Nawaz, H., Khan, I., Maitlo, A., Chhajro, M. A., & Rind, M. M. (2018). Performance Comparison between Merge and Quick Sort Algorithms. *International Journal of Advanced Computer Science and Applications*, 9(11), 192-197. [Link](https://thesai.org/Downloads/Volume9No11/Paper_25-Performance_Comparison_between_Merge_and_Quick_Sort.pdf)

- Aamir, M., Rizvi, S. T. H., Abbas, F., Khan, I., & Akhunzada, A. (2020). Comparative Analysis of Sorting Algorithms in Data Structures: A Review. *IEEE Access*, 8, 125398-125412. [DOI](https://doi.org/10.1109/ACCESS.2020.3006965)
