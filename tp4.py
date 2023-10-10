import numpy as np

def insertionsort(arr):
    i=1
    while i<=len(arr)-1:
        x=arr[i]
        j=i
        while j>0 and arr[j-1] >x:
            arr[j] = arr[j-1]
            j=j-1
            
        arr[j] = x
        i = i+1
    
    return arr


arr=[1,4,2,123,12,432,124,56,7,8,88,0,0,1,1,42]
print(insertionsort(arr))


def siftdown(arr, start, end):
    root = start
    while 2*root + 1 <= end:
        child = 2*root + 1
        sw = root
        if arr[sw] < arr[child]:
            sw = child
        if child + 1 <= end and arr[sw] < arr[child + 1]:
            sw = child + 1
        if sw == root:
            return arr
        else:
            arr[root], arr[sw] = arr[sw], arr[root]
            root = sw
    return arr

def heapify(arr, end):
    start = (end - 1) // 2
    while start >= 0:
        arr = siftdown(arr, start, end)
        start = start - 1
    return arr

arr1 = [1,4,2,421,12,5,6,0,0,0,0,123,11,2,3,5,789,876,233,7,3]
print(heapify(arr1, len(arr1)-1))  # Pass len(arr1)-1 as the end parameter



def heapsort(arr):
    arr = heapify(arr,len(arr)-1)
    end=len(arr)-1
    while end >0:
        arr[end], arr[0] = arr[0], arr[end]
        end = end-1
        arr = siftdown(arr,0,end)
    
    return arr


print(heapsort(arr1))

"""
Question 1: Which of the two sorting algorithms you encoded is more efficient? Can you see why?

Insertion Sort: O(n^2). It becomes inefficient as the size of input increases due to its nested loops for each element.

Heap Sort: O(n log n). Generally more efficient than insertion sort for larger input sizes due to its logarithmic order of growth.

In practice, Heap Sort should generally be more efficient, especially for larger datasets, due to its lower time complexity. """


import time

# Example for Insertion Sort
start_time = time.time()
insertionsort(arr)
end_time = time.time()
execution_time = end_time - start_time
print(f"Insertion sort execution time: {execution_time}")


# Example for Insertion Sort
start_time = time.time()
heapsort(arr)
end_time = time.time()
execution_time = end_time - start_time
print(f"heap sort execution time: {execution_time}")


for l in range(3, 13):  # l between 3 and 12
    n = 2 ** l
    random_arr = np.random.randint(1000, size=n)  # integers [0, 999]

    # Measure times for both algorithms and compare...


import matplotlib.pyplot as plt

# Assume insert_times and heap_times contain execution times
# and sizes contain the respective input sizes

insert_times = []
heap_times = []
sizes = [2**l for l in range(3, 13)]

for n in sizes:
    random_arr = np.random.randint(1000, size=n)
    
    start_time = time.time()
    insertionsort(random_arr.copy())  # .copy() to not sort in-place
    insert_times.append(time.time() - start_time)
    
    start_time = time.time()
    heapsort(random_arr.copy())
    heap_times.append(time.time() - start_time)

plt.plot(sizes, insert_times, label='Insertion Sort')
plt.plot(sizes, heap_times, label='Heap Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.title('Execution Time of Sorting Algorithms')
plt.show()



def sequential_search(arr, target):
    """
    Perform a sequential search on a list.

    Parameters:
    - arr: list of elements
    - target: the element to find

    Returns:
    - index of target in arr if found, otherwise -1
    """
    for i, element in enumerate(arr):
        if element == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

index = sequential_search(arr, target)

if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the array.")


def binary_search(arr, target):
    """
    Perform a binary search on a sorted list.

    Parameters:
    - arr: list of sorted elements
    - target: the element to find

    Returns:
    - index of target in arr if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Element found, return its index
        elif mid_val < target:
            left = mid + 1  # Narrow the search to the right half
        else:
            right = mid - 1  # Narrow the search to the left half
            
    return -1  # Element not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

index = binary_search(arr, target)

if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the array.")



""""
In theory and practice, on sorted arrays, binary search is more efficient than sequential search due to its logarithmic time complexity 
O(logn) as compared to the linear time complexity 
O(n) of sequential search. """

import time
import numpy as np
import matplotlib.pyplot as plt

# Platzhalter für Zeiten
seq_times = []
bin_times = []

# Größen zum Testen
sizes = [2**l for l in range(3, 13)]

# Messungen
num_trials = 100  # Anzahl der Durchläufe pro Größe
for size in sizes:
    seq_time_accum = 0
    bin_time_accum = 0
    
    for _ in range(num_trials):
        arr = np.sort(np.random.randint(1000, size=size))
        target = np.random.randint(1000)
        
        start_time = time.time()
        sequential_search(arr, target)
        end_time = time.time()
        seq_time_accum += (end_time - start_time) * 1000  # Konvertierung in Millisekunden

        start_time = time.time()
        binary_search(arr, target)
        end_time = time.time()
        bin_time_accum += (end_time - start_time) * 1000  # Konvertierung in Millisekunden

    # Durchschnittliche Zeiten speichern
    seq_times.append(seq_time_accum/num_trials)
    bin_times.append(bin_time_accum/num_trials)

# Zeichnen
plt.figure(figsize=[10,6])
plt.plot(sizes, seq_times, marker='o', linestyle='-', label='Sequentielle Suche')
plt.plot(sizes, bin_times, marker='x', linestyle='--', label='Binäre Suche')
plt.xscale('log', base=2)
plt.yscale('log')
plt.xlabel('Array-Größe (log2)')
plt.ylabel('Durchschnittliche Zeit (ms) (log)')
plt.title('Suchzeit im Vergleich zur Array-Größe')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
