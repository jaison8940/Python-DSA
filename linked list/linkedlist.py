class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linkedliststr = ''
        while itr:
            linkedliststr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(linkedliststr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

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
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
                node = Node(data_to_insert, itr.next)
                itr.next = node
            
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.data == data:
            head = head.next 
            return
        
        itr = self.head
        prev = None
        while itr:
            if itr.data == data:
                prev.next = itr.next
            
            prev = itr
            itr = itr.next
        


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_values(["banana","mango","grapes","orange"])
    linkedlist.insert_at(1,"blueberry")
    linkedlist.remove_at(2)
    linkedlist.print()

    linkedlist.insert_values([45,7,12,567,99])
    linkedlist.insert_at_end(67)
    linkedlist.print()
    linkedlist.insert_after_value(7, 22)
    linkedlist.print()
    linkedlist.remove_by_value(22)
    linkedlist.print()
