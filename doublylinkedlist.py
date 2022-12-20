class Node:

	def __init__(self, data):
		self.data = data 
		self.next = None 

class LinkedList:

	def __init__(self):
		self.head = None


	def insertbrgin(self, new_data):

		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node


	def insertatpos(self, prev_node, new_data):

		if prev_node is None:
			print("The given previous node must inLinkedList.")
			return

		new_node = Node(new_data)

		new_node.next = prev_node.next

		prev_node.next = new_node


	def insertend(self, new_data):

		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node


	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data,end=" ")
			temp = temp.next

llist = LinkedList()

llist.insertend(6)

llist.insertbegin(7);

llist.insertbegin(1);

llist.insertbegin(4)

llist.insertatpos(llist.head.next, 8)

print('Created linked list is: ')
llist.printList()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
