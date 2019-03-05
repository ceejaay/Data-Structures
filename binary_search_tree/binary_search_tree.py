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

  def insert(self, value):
      # searching the tree
      searching = True
      # setting current node
      cur_node = self
      # searching
      while searching:
          # if value larger...
          if value > cur_node.value:
              # go left
              # check left for a none cur_node.left
              if cur_node.left == None:
                  # if there is create a node
                  cur_node.left = BinarySearchTree(value)
                  # set searching to false
                  searching = False
                  print('check for left nodes')
              else:
                  # if the cur_node.left is not None.
                  # set the exiisting left node to cur_node
                   cur_node = cur_node.left
          else:
              # we repeat the above only right
              if cur_node.right == None:
                  cur_node.right = BinarySearchTree(value)
                  searching = False
              else:
                  cur_node = cur_node.right


  def contains(self, target):
    pass

  def get_max(self):
    pass




b = BinarySearchTree(50)


b.insert(99)
b.insert(199)
b.insert(9)
print(b.left)
print(b.right)
b.insert(100)
b.insert(2)


