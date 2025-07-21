import random
import time
import sys

# Increase recursion limit for large datasets
sys.setrecursionlimit(500000)

# ------------------------
# Randomized Quicksort
# ------------------------

def randomized_quicksort(arr, low=0, high=None):
    """Sorts the array using Randomized Quicksort (pivot chosen randomly)."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)
    return arr

def randomized_partition(arr, low, high):
    """Partitions the array using a randomly selected pivot."""
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end

    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i  # Return pivot index after partition

# ------------------------
# Deterministic Quicksort (Pivot = First Element)
# ------------------------

def deterministic_quicksort(arr, low=0, high=None):
    """Sorts the array using Deterministic Quicksort (first element as pivot)."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)
    return arr

def deterministic_partition(arr, low, high):
    """Partitions the array using the first element as the pivot."""
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# ------------------------
# Hash Table with Chaining
# ------------------------

class HashTable:
    """Hash table using chaining for collision resolution."""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize empty chains

    def _hash(self, key):
        """Simple hash function (mod table size)."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserts or updates the key-value pair."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.table[index].append([key, value])  # Add new key

    def search(self, key):
        """Searches for a key and returns the associated value if found."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        """Deletes the key-value pair if found."""
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]

# ------------------------
# Quicksort Comparison Runner
# ------------------------

def compare_quicksorts(datasets, size):
    """Runs and compares Randomized vs Deterministic Quicksort on multiple datasets."""
    print(f"\n=== Quicksort Performance Comparison (Input Size = {size}) ===\n")
    for description, dataset in datasets:
        data1 = dataset.copy()  # Copy for Randomized Quicksort
        data2 = dataset.copy()  # Copy for Deterministic Quicksort

        print(f"\nDataset: {description} (Size = {len(dataset)})")

        # Run Randomized Quicksort
        start = time.time()
        randomized_quicksort(data1)
        random_time = time.time() - start

        # Run Deterministic Quicksort
        start = time.time()
        try:
            deterministic_quicksort(data2)
            deterministic_time = time.time() - start
            deterministic_status = f"{deterministic_time:.6f} seconds"
        except RecursionError:
            deterministic_status = "RecursionError / Failed"

        # Output results
        print(f"Randomized Quicksort:   {random_time:.6f} seconds")
        print(f"Deterministic Quicksort: {deterministic_status}")

# ------------------------
# Main Execution Block
# ------------------------

if __name__ == "__main__":

    input_sizes = [10000, 20000, 30000]  # Sizes to test scalability

    for SIZE in input_sizes:
        # Prepare datasets of different types
        datasets = [
            ("Random Array", [random.randint(0, SIZE) for _ in range(SIZE)]),
            ("Array with Repeated Elements", [random.choice([1, 2, 3, 4, 5]) for _ in range(SIZE)]),
            ("Sorted Array", list(range(SIZE))),
            ("Reverse Sorted Array", list(range(SIZE, 0, -1)))
        ]


        # Run Quicksort comparisons on all datasets for current SIZE
        #compare_quicksorts(datasets, SIZE)

    # Demonstrate Hash Table functionality once
    print("\n\n=== Hash Table Demo ===")
    ht = HashTable(size=20)

    # Insert elements into the hash table
    for key in ['apple', 'banana', 'cherry', 'date', 'berry']:
        ht.insert(key, len(key))

    print("Search 'banana':", ht.search('banana'))
    ht.delete('banana')
    print("Search 'banana' after deletion:", ht.search('banana'))

    print("\nHash Table Internal State:")
    for index, chain in enumerate(ht.table):
        print(f"Slot {index}: {chain}")
