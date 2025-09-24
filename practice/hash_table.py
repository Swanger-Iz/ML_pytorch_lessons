# class HashTable:

#     def __init__(self, capablicity=10):
#         self.MAX = capablicity
#         self.arr = [[] for i in range(self.MAX)]

#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
    
    
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for i, el in enumerate(self.arr[h]):
#             # print(el[0])
#             if el[0] == key:
#                 return el[1]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False

#         for idx, el in enumerate(self.arr[h]):
#             if len(el) == 2 and el[0]==key:
#                 self.arr[h][idx] = (key, val)
#                 found=True
#                 if found == True: break
#         if not found:
#             self.arr[h].append((key, val))
            

#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         for i, el in enumerate(self.arr[h]):
#             # print(el[0])
#             if el[0] == key:
#                 del self.arr[h][i]
                


class HashTable_LP:

    def __init__(self, capablicity=10):
        self.MAX = capablicity
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        #return self.arr[h]
        pass
        
        
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # self.arr[h] = val
        
        if self.arr[h] is None:
            self.h = (key, val)
        else:
            pass







t = HashTable_LP()
# t.arr[0] = 9999
t['march 6'] = 228
t['march 8'] = 1111
print(t.arr)

t['march 17'] = 1337
print(t.arr)
print(t['march 17'])
















# ht = HashTable()
# # print(ht.add('march 6', 120))
# # print(ht.get('march 6'))
# elements = 5
# # for i in range(elements):
# #     ht[str('march ' + str(i))] = 5 * i


# # print(str('march ' + str(5)))
# # print(ht.arr)
# ht['march 6'] = 228
# ht['march 17'] = 500
# print(ht.arr)
# del ht['march 17']
# print(ht.arr)
# #print(ht['march 17'])

# # print(ht['march 6'], ht['march 17'])