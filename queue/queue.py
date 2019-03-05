
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail




    def insert_head(self, value):
        # make a new node
        n = Node(value)
        # if there is no head or tail. Make the new node the head and tail
        if self.head == None and self.tail == None:
            self.head = n
            self.tail = n
            n.next_node = None
            # print('add with nothing in list')
            # print('head', self.head.value)
            # print('tail', self.tail.value)
            # print('********')
        else:
            n.next_node = self.head
            self.head = n
            # print('head', self.head.value)
            # print('tail', self.tail.value)
            # print('********')




    def pop(self):
        current_node = self.head
        # print('tail before', self.tail.value)
        while current_node.next_node.get_next():

            print('checking current node', current_node.value)
            current_node = current_node.next_node


        print('current_node.next_node.value:', current_node.next_node.value)
        last_node = current_node.next_node.value
        # print('last node before pop', last_node)
        self.tail = current_node
        current_node.next_node = None
        # print('new tail', self.tail.value)
        return last_node

        # set a flag at the head
        # check the next node.
        # if it is equal to the tail, the we know that the flagged node is the second to last.
        #     Then we set the second to last node to the last node.
        #     We change the second to last node's next_node to None
        # So while the flagged node.get_next is not equal to the tail. We change the flagged node to the flagged node.next_node

        # check the next node
        # if it is the tail



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
        if self.next_node == None:
            return False
        else:
            return True


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
      self.size -= 1
      return self.storage.pop()


  def len(self):
      return self.size


q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print('size', q.size)
print('pop 100?', q.dequeue())
print('size', q.size)
print('pop 101?', q.dequeue())
print('size', q.size)
print('pop 105?', q.dequeue())
print('size', q.size)



