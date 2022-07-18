class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None
   
  def append(self, value):
    if self.head = None:
      self.head = Node(value)
    else:
      current_node = self.head
      while current_node.next:
        current_node = current_node.next
      current_node.next = Node(value)
