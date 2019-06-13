class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.insert(len(self.storage), value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    element = self.storage
    element[0], element[len(element) - 1] = element[len(element) - 1], element[0]
    j = element.pop(len(element) - 1)
    self._sift_down(0)
    return j

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
    pass
