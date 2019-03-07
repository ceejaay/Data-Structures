class Heap:
    def __init__(self):
        self.storage = []
# self.storage = [999, 67, 81, 43, 51, 78, 54, 24, 27, 30, 1]

    def insert(self, value):
        self.storage.append(value)
# print('last value', self.storage(len(self.storage)))
        return self._bubble_up(len(self.storage) -1)


    def delete(self):
        if len(self.storage) == 0:
            return "empty array"
        else:
            # last_index =  self.storage[len(self.storage) - 1]
# last index will be 1
# this swaps 1 and 999
            self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1],  self.storage[0]
# this pops 999

        last_value = self.storage.pop(-1)
# call sift down
        self._sift_down(0)
        return last_value
# print(self.storage)




    def get_max(self):
        print('get max', self.storage)
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
# print(f'new_value: {self.storage[new_value]} new value index: {new_value}, parent index: {parent}, parent value: {self.storage[parent]}', )kk

# print('top value: ', self.storage[0])
        print('array', self.storage)

    def _sift_down(self, index):
        parent = index
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        if left_child > len(self.storage) - 1:
            return
        if right_child > len(self.storage) - 1:
            return
        if self.storage[parent] > self.storage[left_child] and self.storage[parent] > self.storage[right_child]:
            # print('check if parent is larger', self.storage)
            return
        if self.storage[left_child] >= self.storage[right_child]:
            self.storage[left_child], self.storage[parent] = self.storage[parent], self.storage[left_child]
            self._sift_down(left_child)
        else:
            self.storage[right_child], self.storage[parent] = self.storage[parent], self.storage[right_child]
            self._sift_down(right_child)
        # print('at the end of the sift down', self.storage)






# left 2i + 1
# right 2i + 2
# the value at 0 is 1
# parent == 0
# parent = index
# # get last index which is 9
# last_index = len(self.storage) - 1
# # while 1 < 30
# while self.storage[parent]< self.storage[last_index]:

#     left_child = 2 * parent + 1
#     right_child = 2 * parent + 2
#     if self.storage[left_child] > self.storage[right_child]:
#        self.storage[left_child], self.storage[parent] = self.storage[parent], self.storage[left_child]
#        parent = left_child
#        print(f"p: {self.storage[index]}, L: {self.storage[left_child]} R: {self.storage[right_child]}")
#        print(self.storage)
#     else:
#         self.storage[right_child], self.storage[parent] = self.storage[parent], self.storage[right_child]
#         parent = right_child 
#         print(f"p: {self.storage[index]}, L: {self.storage[left_child]} R: {self.storage[right_child]}")
#         print(self.storage)

h = Heap()
# print(h.insert(999))
# print(h.storage)
# print(h.delete())

h.insert(6)
h.insert(8)
h.insert(10)
h.insert(9)
h.insert(1)
h.insert(9)
h.insert(9)
h.insert(5)
print(h.get_max())
h.delete()
print(h.get_max())
h.delete()
print(h.get_max())

