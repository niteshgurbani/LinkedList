class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.Head = new_node
        self.Tail = new_node
        self.length = 1

    def append(self, value):
        appending_node = Node(value)
        if self.length == 0:
            self.Head = appending_node
            self.Tail = appending_node
        else:
            self.Tail.next = appending_node
            appending_node.prev = self.Tail
            self.Tail = appending_node
        self.length += 1
    
    def prepend(self,value):
        prepending_node = Node(value)
        if self.length == 0:
            self.Tail = prepending_node
            self.Head = prepending_node
        else:
            self.Head.prev = prepending_node
            prepending_node.next = self.Head
            self.Head = prepending_node
        self.length +=1

    # pop function removing the last value
    #tail.prev = tail, tail.next = None
    def pop(self):
        if self.length <= 0:
            return None
        temp = self.Tail
        if self.length == 1:
            self.Head = None
            self.Tail = None
        else:    
            self.Tail = temp.prev
            self.Tail.next = None
            temp.prev = None #for garbage collection, not neccessary
        self.length -= 1
        return temp.value
    
    def pop_first(self):
        if self.length <=0:
            return None
        temp = self.Head
        if self.length ==1:
            self.Head = None
            self.Tail = None
        else:
            self.Head = temp.next
            self.Head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value            

    def print_list(self):
        temp = self.Head
        while temp:
            print(temp.value, end=" <-> " if temp.next else "")
            temp = temp.next
        print()


dll = DoublyLinkedList(10)
dll.append(20)
dll.prepend(5)
dll.append(30)
dll.prepend(1)
dll.print_list()
# Output should be: 1 <-> 5 <-> 10 <-> 20 <-> 30
