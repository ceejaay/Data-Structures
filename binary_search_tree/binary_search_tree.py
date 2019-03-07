
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    # alternate plan:
    #     inside insert we set a current_node and a searching variable.
    #     current_node = self
    #     searching = true
    #     while searching:
    #         if value > current_node.value:
    #             go left
    #             if left has none.
    #             create a node.
    #             set searching to false
    #             if it has a node.
    #                 then current_node = current_node.left
    # recursive plan
    #     check the first value wich is the current node
        # if value > self.value

  def insert(self, value):
      if value < self.value:
          if self.left == None:
              self.left = BinarySearchTree(value)
              # print('inserted', value)
          else:
              self.left.insert(value)
      else:
          if self.right == None:
              self.right = BinarySearchTree(value)
              # print('inserted', value)
          else:
              self.right.insert(value)


  def contains(self, target):
      if target == self.value:
          return True
      elif target < self.value:
          if target == self.left.value:
              return True
          else:
              return self.left.contains(target)
      elif target > self.value:
          if target == self.right.value:
              return True
          else:
              return self.right.contains(target)

  def get_max(self):
      pass




b = BinarySearchTree(5)
b.insert(2)
b.insert(3)
b.insert(7)
b.insert(6)
print('contains: ', b.contains(7))

# print('left: ', b.left.value)
# print('left then right value: ', b.left.right.value)
# print('right then left value: ', b.right.left.value)
# print(b.right.value)


      # # searching the tree
      # searching = True
      # # setting current node
      # cur_node = self
      # # searching
      # while searching:
      #     # if value larger...
      #     if value > cur_node.value:
      #         # go left
      #         # check left for a none cur_node.left
      #         if cur_node.left == None:
      #             # if there is create a node
      #             cur_node.left = BinarySearchTree(value)
      #             # set searching to false
      #             searching = False
      #             print('check for left nodes')
      #         else:
      #             # if the cur_node.left is not None.
      #             # set the exiisting left node to cur_node
      #              cur_node = cur_node.left
      #     else:
      #         # we repeat the above only right
      #         if cur_node.right == None:
      #             cur_node.right = BinarySearchTree(value)
      #             searching = False
      #         else:
      #             cur_node = cur_node.right
