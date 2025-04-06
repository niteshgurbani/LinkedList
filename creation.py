class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.Head = new_node
        self.Tail = new_node
        self.length = 1

#append in the beginning
    def prepend(self,value):
        prepending_node = Node(value)
        prepending_node.next = self.Head
        self.Head = prepending_node
        self.length += 1

    def append(self,value):
        appending_node = Node(value)
        self.Tail.next = appending_node
        self.Tail = appending_node
        self.length += 1

    def pop_first(self):
        if self.Head is None:
            return None  # if list is empty

        temp = self.Head
        self.Head = self.Head.next
        temp.next = None
        if self.Head is None:
            self.Tail = None
        self.length -= 1
        return temp.value # returning popped value
    
    def pop(self):
        #edge cases
        
        #list is empty
        if self.Head is None:
            return None
                
        #list has one item
        if self.Head.next is None:
            temp = self.Head
            self.Head = None
            self.Tail = None
            temp.next = None
            self.length -= 1
            return temp.value
        
        
        #normally
        temp = self.Head
        while temp.next.next is not None:
            temp = temp.next
        popped_node = temp.next
        temp.next = None
        self.Tail = temp
        self.length -= 1
        return popped_node.value


    def print_list(self):
        temp = self.Head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def set_value(self, index, value):
        node_to_change = self.get(index)
        if node_to_change:
            node_to_change.value = value
            return True
        return False

    def insert(self, index, value):
        if index>self.length or index<0:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        
        temp = self.Head
        new_node = Node(value)
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        



    def get(self,index):
        #edge cases
        if self.length == 0 or index>=self.length or index<0:
            return None
        
        temp = self.Head
        for _ in range(0,index):
            temp = temp.next
        return temp

    def reverse(self):
        if self.length<=1:
            return
        
        before = None
        current = self.Head
        self.Tail = self.Head

        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after
            
        self.Head = before


# new_linkedlist = LinkedList(5)
# new_linkedlist.prepend(4)
# new_linkedlist.append(6)
# print(new_linkedlist.pop_first())
# new_linkedlist.print_list()

new_linkedlist = LinkedList(10)
new_linkedlist.append(20)
new_linkedlist.append(30)
new_linkedlist.insert(0, 5)     # Insert at start
new_linkedlist.insert(2, 15)    # Insert in middle
new_linkedlist.insert(5, 35)    # Insert at end
new_linkedlist.insert(100, 999) # Invalid index

new_linkedlist.print_list()
print("Length:", new_linkedlist.length)