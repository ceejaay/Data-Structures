
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail




    def insert_head(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
            n.next_note = None
        else:
            n.next_node = self.head
            self.head = n




    def pop(self):
        # set a flag at the head
        # check the next node.
        # if it is equal to the tail, the we know that the flagged node is the second to last.
        #     Then we set the second to last node to the last node.
        #     We change the second to last node's next_node to None
        # So while the flagged node.get_next is not equal to the tail. We change the flagged node to the flagged node.next_node

        # check the next node
        # if it is the tail
        current_node= self.head
        while current_node.get_next is not self.tail:
            current_node = current_node.get_next

        self.tail = current_node
        self.tail.next_node = None



            # current_node
        # if current_node.next_node == None:
            # self.tail = current_node
            # current_node.next_node = None
        # else:
            # current_value = current_value.next_node
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next(self):
        return self.next_node


class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
      self.storage.insert_head(item)
      self.size += 1
      return item

    # value gets passed intVo a new node.
    # we have to add to the length as well



  def dequeue(self):
      pass

  def len(self):
      return self.size


q = Queue
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q.size)



