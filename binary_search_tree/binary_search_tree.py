# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      # check the value.
      # if larger go left
      # else go right.
      #     check left or right for none. 
      #     if it has none.
      #         then create a new Binary search tree object where there was non.
      #   If self.left or self.right does not == none. 
      #   Then check the child node for left/right none.
      if value > self.value:
          if self.left == None:
              self.left = BinarySearchTree(value)
          else:

          print('larger')
      else:
          print('smaller')



  def contains(self, target):
    pass

  def get_max(self):
    pass




b = BinarySearchTree(50)


b.insert(99)
b.insert(9)
print(b.left.value)

