class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next # pointer that contains data and next_pointer

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        while itr.next: itr = itr.next # we have a last el. if we get a Null
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_len(self):
        count = 0
        itr = self.head
        while itr: 
            itr = itr.next
            count += 1
        return count
    
    def remove_el(self, idx):
        if (idx < 0 or idx > self.get_len()):  # and not (idx == -1)
            raise Exception('Invalid index')
        
        
        if not self.head: 
            print('Linked list is empty')
            return
        
        if idx == 0:
            self.head = self.head.next
            print(f"Deleted element: {self.head.data}")
            return
        
        # init necessary vars
        counter = 0
        itr = self.head
        
        if idx == 0:
            self.head = itr.next
            print(f"Deleted element: {itr.data}")
            return
        
        # finding the element
        while itr:
            if counter == idx-1:
                el = itr.next
                itr.next = itr.next.next
                break
                
                # one_before_last = itr
                # counter += 1
            # if counter == idx+1:
            #     next_el = itr
            #     counter += 1
            
            itr = itr.next
            counter += 1
        print(f"Deleted element: {el.data}")
        del el
        # one_before_last.next = next_el.next
        return
    
    def insert_val(self, idx, data):
        if idx == -1: self.insert_at_end(data); return
        if idx == 0: self.insert_at_begining(data); return
        if idx < 0 or idx > self.get_len(): raise Exception("Invalid Index")

        if idx == 0: self.insert_at_begining(data)
        
        itr = self.head
        counter = 0
        
        while itr:
            if idx-1 == counter:
                # print(itr.next.next.data)
                itr.next = Node(data, itr.next)
                break
            counter += 1
            itr = itr.next
        
    def insert_after_value(self, data_after, data_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_insert, itr.next)
                return
            itr = itr.next
            
        raise Exception(f"no data like: {data_after}")
    
    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                to_del = itr.next
                itr.next = itr.next.next
                del to_del
                return
            
            itr = itr.next
        
        
        
        
if __name__ == '__main__':
    ll = LinkedList()
    
    
    ll.insert_values([229, 228, 1337, 1488, 123, 12444])
    ll.insert_after_value(229, 'fuck')
    ll.print()
    print(ll.get_len())
    
    ll.remove_by_value(1488)
    
    ll.print()
    print(ll.get_len())
    
    # print(f"calling: {ll.insert_val.__name__}")
    # ll.insert_val(2, 'ass')
    # ll.print()
    # print(ll.get_len())
    
    # ll.insert_val(5, 'ass2')
    # ll.print()
    # print(ll.get_len())
    
    

