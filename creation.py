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

    def get(self,index):
        #edge cases
        if self.length == 0 or index>=self.length or index<0:
            return None
        
        temp = self.Head
        for _ in range(0,index):
            temp = temp.next
        return temp




new_linkedlist = LinkedList(5)
new_linkedlist.prepend(4)
new_linkedlist.append(6)
print(new_linkedlist.pop_first())
new_linkedlist.print_list()

