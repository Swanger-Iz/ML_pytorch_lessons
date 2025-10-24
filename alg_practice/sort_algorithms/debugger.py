def find_min(arr):
    min = arr[0]
    idx = 0
    for i in range(len(arr)):
        if arr[i] < min: 
            min = arr[i]
            idx = i
    return min, idx

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_i = i
        for j in range(min_i+1, size):
            if arr[j] < arr[min_i]: min_i = j

        if i != min_i: arr[i], arr[min_i] = arr[min_i], arr[i]
    
    
elements = [78, 12, 15, 8, 61, 53, 23, 27]
print(elements)
selection_sort(elements)
print(elements)