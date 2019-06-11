"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head != None:
        self.head.insert_before(value)
        self.head = self.head.prev
    else:
        self.head = ListNode(value)
        self.tail = self.head
    self.length += 1
    # if not self.head and not self.tail:
    #     new_node = ListNode(value)
    #     self.head = new_node
    #     self.tail = new_node
    # else:
    #     new_node = ListNode(value)
    #     self.head.insert_before(new_node)
    #     self.head = new_node


  def remove_from_head(self):
    if self.head == None:
        self.tail = None
        self.length = 0
        head_capture = None
    else:
        new_head = self.head.next 
        head_capture = self.head.value
        self.head.delete()
        self.head = new_head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return head_capture

  def add_to_tail(self, value):
    if self.tail != None:
        self.tail.insert_after(value)
        self.tail = self.tail.next
    else:
        self.tail = ListNode(value)
        self.head = self.tail
    self.length += 1

  def remove_from_tail(self):
    if self.tail == None:
        self.head = None
        self.length = 0
        head_capture = None
    else:
        new_tail = self.tail.prev
        head_capture = self.tail.value
        self.tail.delete()
        self.tail = new_tail
        self.length -= 1
        if self.length == 0:
            self.head = None
    return head_capture

  def move_to_front(self, node):
    self.head.prev = node

    if self.tail == node:
        self.remove_from_tail()
        self.length += 1
    else:
        node.delete()
    node.next = self.head
    self.head = node

  def move_to_end(self, node):
    self.tail.next = node

    if self.head == node:
        self.remove_from_head()
        self.length += 1
    else:
        node.delete()
    node.prev = self.tail
    self.tail = node

  def delete(self, node):
    if self.head == node:
        self.remove_from_head()
    elif self.tail == node:
        self.remove_from_tail()

  def get_max(self):
    if self.head == None:
        return None
    max_list = self.head.value
    node = self.head
    for x in range(self.length - 1):
        if node != None:
            node = node.next
            if node.value > max_list:
                max_list = node.value
    return max_list
