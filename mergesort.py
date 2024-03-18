def merge_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        mid = len(arr)//2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)
    
def merge(left_half, right_half):
    merged_arr = []
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            merged_arr.append(left_half.pop(0))
        else:
            merged_arr.append(right_half.pop(0))
    merged_arr.extend(left_half)
    merged_arr.extend(right_half)
    return merged_arr

arr = [6,3,1,4,3,2,5]
arr = merge_sort(arr)
print(arr)