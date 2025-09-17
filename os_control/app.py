import os

def return_files(dir):
    result_list = []
    files = os.listdir(dir)
    
    for item in files:
        
        if os.path.isdir(os.path.join(dir, item)): result_list.extend(return_files(os.path.join(dir, item)))
        else: result_list.append(item)
    return result_list
        
 


    
dir_name = '.'
print(return_files(dir_name))





























print('Done')




