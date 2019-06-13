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
    current_node = self
    answer = False

    while True:
        if current_node.value == target:
            answer = True
            break
        elif current_node.value > target:
            if current_node.left is not None:
                current_node = current_node.left
            else:
                break
        elif current_node.value < target:
            if current_node.right is not None:
                current_node = current_node.right
            else:
                break
    return answer


  def get_max(self):
    if self.right == None:
        return self.value
    return self.right.get_max()

  def for_each(self, cb):
    if self.left != None:
        self.left.for_each(cb)
    elif self.right != None:
        self.right.for_each(cb)
    return cb(self.value)