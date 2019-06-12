class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value and self.left:
        self.left.insert(value)
    elif value < self.value:
        self.left = BinarySearchTree(value)
    elif value > self.value and self.right:
        self.right.insert(value)
    elif value > self.value:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass