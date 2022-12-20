class Node:
	def __init__(self, data):
		self.data = data
		self.next = 0


class CircularLinkedList:
	def __init__(self):
		self.last = None

	def addToEmpty(self, data):
		if (self.last != None):
			return self.last
		temp = Node(data)
		self.last = temp
		self.last.next = self.last
		return self.last

	def addBegin(self, data):
		if (self.last == None):
			return self.addToEmpty(data)
		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp
		return self.last

	def addEnd(self, data):
		if (self.last == None):
			return self.addToEmpty(data)
		temp = Node(data)
		temp.next = self.last.next
		self.last.next = temp
		self.last = temp
		return self.last

	def addAfter(self, data, item):

		if (self.last == None):
			return None

		temp = Node(data)
		p = self.last.next
		while p:
			if (p.data == item):
				temp.next = p.next
				p.next = temp

				if (p == self.last):
					self.last = temp
					return self.last
				else:
					return self.last
			p = p.next
			if (p == self.last.next):
				print(item, "not present in the list")
				break

	def traverse(self):
		if (self.last == None):
			print("List is empty")
			return
		temp = self.last.next
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
			if temp == self.last.next:
				break
  def DeleteFirst(head):
    previous = head
    next = head
 
    if (head == None) :
     
        print("\nList is empty")
        return None
     
    if (previous.next == previous) :
     
        head = None
        return None
     
    while (previous.next != head):
        previous = previous.next
        next = previous.next
     
    previous.next = next.next
 
    head = previous.next
 
    return head
 
def DeleteLast(head):
    current = head
    temp = head
    previous = None
 
    if (head == None):
        print("\nList is empty")
        return None
 
    if (current.next == current) :
        head = None
        return None
 
    while (current.next != head):
        previous = current
        current = current.next
     
    previous.next = current.next
    head = previous.next
     
    return head
 

def DeleteAtPosition(head, index):
 
    len = Length(head)
    count = 1
    previous = head
    next = head
 
    if (head == None):
        print("\nDelete Last List is empty")
        return None
     
    if (index >= len or index < 0) :
        print("\nIndex is not Found")
        return None
 
    if (index == 0) :
        head = DeleteFirst(head)
        return head
 
    while (len > 0):
     
        if (index == count):
            previous.next = next.next
             
            return head
         
        previous = previous.next
        next = previous.next
        len = len - 1
        count = count + 1
     
    return head

if __name__ == '__main__':
	llist = CircularLinkedList()
	last = llist.addToEmpty(6)
	last = llist.addBegin(4)
	last = llist.addBegin(2)
	last = llist.addEnd(8)
	last = llist.addEnd(12)
	last = llist.addAfter(10, 8)
	llist.traverse()
