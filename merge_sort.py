def merge(arr, m, l, r):
    left_arr = arr[l:m+1]
    right_arr = arr[m+1:r+1]
    i = 0
    j = 0
    k = l

    while i < len(left_arr) and j < len(right_arr):
        
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, m, l, r)
    
arr = [12, 11, 13, 5, 6, 7] 
array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(arr, 0, len(array) -1)
print(arr)
