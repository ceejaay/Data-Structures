class Heap:
  def __init__(self):
    self.storage = []
    # self.storage = [98, 67, 81, 43, 51, 78, 54, 24, 27, 30, 26]

  def insert(self, value):
      self.storage.append(value)
      # print('last value', self.storage(len(self.storage)))
      return self._bubble_up(len(self.storage) -1)


  def delete(self):
      self.storage.pop(0)
      return self._bubble_up(len(self.storage) -1)

  def get_max(self):
      return self.storage[0]

  def get_size(self):
    return len(self.storage)
    # pass

  def _bubble_up(self, index):
      # find the parent
      parent = (index - 1) // 2
      new_value = index
      while self.storage[parent] < self.storage[new_value] and new_value > 0:
          self.storage[parent], self.storage[new_value] = self.storage[new_value], self.storage[parent]
          new_value = parent
          parent = (new_value - 1) // 2
          # print(f'new_value: {self.storage[new_value]} new value index: {new_value}, parent index: {parent}, parent value: {self.storage[parent]}', )

      # print('top value: ', self.storage[0])
      # print('array', self.storage)




  def _sift_down(self, index):
      pass



# h = Heap()
# print(h.insert(999))
# print(h.storage)


