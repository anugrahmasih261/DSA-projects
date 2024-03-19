# linear search
def linear_search(arr):
    target = int(input('Enter num to search='))
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Return the index immediately when the target is found
    return -1 # Return -1 if the target is not found

arr = [1,2,3,4,5,67]
index = linear_search(arr)
if index != -1:
    print('found at index',index)
else:
    print('not found in array')