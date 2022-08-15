class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        
        self.prev = prev
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linkliststr = ''
        while itr:
            linkliststr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(linkliststr)
    
    def print_backward(self):
        if self.tail is None:
            print("Linked list is empty")
            return
        itr = self.tail
        linkliststr = ''
        while itr:
            linkliststr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(linkliststr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, None, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head,self.tail = node, node
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        node = Node(data, itr, None)
        itr.next = node
        self.tail = node

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr, itr.next)
                itr.next.prev = node
                itr.next = node
            
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.data == data:
            head = head.next
            head.prev = None
            return
        
        itr = self.head
        prev = None
        while itr:
            if itr.data == data:
                prev.next = itr.next
                itr.next.prev = prev
            
            prev = itr
            itr = itr.next
        


if __name__ == '__main__':
    linklist = LinkedList()
    linklist.insert_values(["banana","mango","grapes","orange"])
    linklist.insert_at(1,"blueberry")
    linklist.remove_at(2)
    linklist.print_forward()
    linklist.print_backward()

    linklist.insert_values([45,7,12,567,99])
    linklist.insert_at_end(67)
    linklist.print_forward()
    linklist.print_backward()
    linklist.insert_after_value(7, 22)
    linklist.print_forward()
    linklist.print_backward()
    linklist.remove_by_value(22)
    linklist.print_forward()
    linklist.print_backward()
