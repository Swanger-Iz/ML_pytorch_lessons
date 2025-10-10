def bubble_sort(arr):
    size = len(arr)
    swapped = False
    
    while size != 0:
        for i in range(size-1):
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
         
        if not swapped: break     
        size -= 1
    
    return arr
    
# sarr = [2, 4, 6]
# elems = [5, 9, 2, 1, 67, 34, 88, 34]
# print(bubble_sort(sarr))





def bb_sort(arr, key):
    size = len(arr)
    # my_vals = [el[key] for el in arr]
    
    for i in range(size-1):
        if arr[i][key] > arr[i+1][key]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    
    return arr

# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# (bb_sort(elements, 'name'))



def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor
    return arr

elems = [5, 9, 2, 1, 67, 34, 88, 34]
print(insertion_sort(elems))




