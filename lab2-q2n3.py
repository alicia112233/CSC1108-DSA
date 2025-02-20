class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # return the value of the node at index
    def search(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1
        if temp is None:
            print('search error: invalid index')
        else:
            return temp
        
    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def delete(self, value):
        prev = None
        temp = self.head
        while temp != None and temp.data != value:
            prev = temp
            temp = temp.next
        
        # node to be deleted is head
        if temp == self.head:
            self.deleteAtHead()
        
        # Value found
        elif temp != None:
            prev.next = temp.next
            del temp
        
        # Value not found
        else:
            print('Value ', value, ' cannot be found')

    # delete the node at index
    def deleteAt(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('search error: invalid index')
        else:
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
            del temp

    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def printList(self):
        print("Current list content:")
        temp = self.head
        while temp is not None:
            print("data = ", temp.data)
            temp = temp.next
        print()

    # return the number of elements in the queue
    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size
    
class Queue:
    def __init__(self):
        # You must implement this Queue with a SinglyLinkedList
        self.q = SinglyLinkedList()

    def enqueue(self, value):
        s = SinglyListNode(value)
        self.q.insertAtHead(s)

    def printQueue(self):
        self.q.printList()

    def dequeue(self):
        last = self.q.size() - 1
        value = self.q.search(last).data
        self.q.deleteAt(last)
        return value
    
    def isEmpty(self):
        return self.q.size() == 0
    
    def peek(self):
        last = self.q.size() - 1
        return self.q.search(last).data

Q = Queue()
print("Is Q empty? - ", Q.isEmpty())
Q.enqueue(8)
print("After enqueuing: 8")
Q.printQueue()
print("After enqueuing: -5")
Q.enqueue(-5)
Q.printQueue()
print("perform dequeue() to remove ", Q.dequeue())
print("After dequeing")
Q.printQueue()
print("After enqueuing: 2")
Q.enqueue(2)
Q.printQueue()
print("perform peek() = ", Q.peek())
print("perform dequeue() to remove ", Q.dequeue())
print("After dequeing")
Q.printQueue()
print("Is Q empty? - ", Q.isEmpty())
print("perform peek() = ", Q.peek())
print("perform dequeue() to remove ", Q.dequeue())
print("After dequeing")
Q.printQueue()

# queue ADT using SinglyLinkedList