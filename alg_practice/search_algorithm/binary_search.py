# Decorators 

    # import time

    # def time_of_function(func):
    #     def wrapper(*args, **kwargs):
    #         start = time.time()
    #         print(func())
    #         end = time.time()
    #         result = end - start
    #         print(f'Execution time: {result * 1000:.4f}')
    #         return 'Wrapper result'
    #     return wrapper

    # @time_of_function
    # def func1():
    #     my_list = [i for i in range(1, 1000000)]
    #     return 228

    # @time_of_function
    # def func2():
    #     my_list = [i for i in range(1, 1000000)]
        

    # print(func1())

    # func2()


def linear_search(nums_list, num_to_find):
    for i, val in enumerate(nums_list):
        if val == num_to_find: return i
    return -1

def binary_search_loop(nums_list, num_to_find):
    
    left_index = 0
    right_index = len(nums_list) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        
        if num_to_find == nums_list[mid_index]: return mid_index
        
        if num_to_find > nums_list[mid_index]: left_index = mid_index + 1
        
        if num_to_find < nums_list[mid_index]: right_index = mid_index
        
    return mid_index
        

def binary_search_rec(nums_list, num_to_find, start_idx=0, end_idx=None):
    
    left_index = start_idx
    right_index = len(nums_list) - 1 if end_idx is None else end_idx
    mid_index = (left_index + right_index) // 2
    
    
    if num_to_find == nums_list[mid_index]: return mid_index
    
    if num_to_find > nums_list[mid_index]: return binary_search_rec(nums_list, num_to_find, mid_index+1, right_index)
        
    if num_to_find < nums_list[mid_index]: return binary_search_rec(nums_list, num_to_find, left_index, mid_index)
    
def find_all_occurances(nums, num_to_find):
    index = binary_search_rec(nums, num_to_find)
    indices = [index]
    
    # check left side 
    i = index - 1
    while i >= 0:
        if numbers[i] == num_to_find: indices.append(i)
        else: break
        i -= 1
    
    i = index + 1
    while i < len(numbers):
        if numbers[i] == num_to_find: indices.append(i)
        else: break
        i += 1
    
    return sorted(indices)
            

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]  # len = 8
val = 15
idx = find_all_occurances(numbers, val)

print(numbers)
print(f'Looking for value: {val}, Index: {idx}')

print('-' * 20)



