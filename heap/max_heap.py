class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.insert(len(self.storage), value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # store max value in a variable so we can return it later
    element = self.storage[0]
    # replace the first storage element with the last element in the heap
    self.storage[0] = self.storage[len(self.storage) - 1]
    # remove the last element in the heap
    self.storage.pop()
    # call sift_down in order to move the element at index 0 down to a valid spot in the heap
    self._sift_down(0)
    return element

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    element = self.storage
    b = ((index - 1) // 2)
    if b >= 0:
        if element[index] > element[b]:
            element[index], element[b] = element[b], element[index]
            self._bubble_up(b)
        else:
            return
    else:
        return

  def _sift_down(self, index):
    end = len(self.storage) - 1
    child = index * 2 + 1

    while child <= end:
        rchild = child + 1
        # check if rchild has higher priority than the left child
        if rchild <= end and self.storage[rchild] > self.storage[child]:
            child = rchild
        # check if parent has lower priority than child
        if self.storage[child] > self.storage[index]:
            self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
            index = child
            child = 2 * index + 1
        else:
            break
