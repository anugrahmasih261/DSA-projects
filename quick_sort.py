def quick_sort(arr):
    # Base case: if the length of the array is 1 or less, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (in this case, the middle element)
    pivot = arr[len(arr) // 2]

    # Divide the array into three sub-arrays: left, middle, and right
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to pivot
    right = [x for x in arr if x > pivot]      # Elements greater than pivot

    # Recursively sort the left and right sub-arrays, then combine them with the middle array
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]

# Print original array
print("Original Array:", arr)

# Sort the array using Quick Sort
sorted_arr = quick_sort(arr)

# Print sorted array
print("Sorted Array:", sorted_arr)


# Explanation of time and space 
'''
Time Complexity: The average time complexity of Quick Sort is O(n log n), 
where n is the number of elements in the array. However, 
in the worst-case scenario (when the pivot is not well chosen), it can degrade to O(n^2).
Space Complexity: The space complexity of Quick Sort is O(log n) 
in the best and average cases due to the recursive calls. In the worst case, it can be O(n) due to the recursion depth.
'''
