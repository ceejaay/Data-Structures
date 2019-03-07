
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
        # keep track of current node
        current_node = self.head
        # keep track of the last node
        last_node = self.head
        # searching is true
        searching = True
        while searching:
            if current_node.next_node == None:
                searching = False
                print('last node', last_node.value)
                print('last node next node', last_node.next_node.value)
                last_node.next_node = None
                print('last node', last_node.value)
                return last_node.value
            else:
                last_node = current_node
                current_node = current_node.next_node

            # print('looking for tail')
            # current_node = current_node.next_node
            # print('current node next node', current_node.next_node.value)
        # if current_node.value != None:
            # self.tail = current_node
            # current_node.next_node = None
        # # print('current node value', current_node.value)
        # return current_node.value

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
      # print('len after enqueue', self.len())
      return item

    # value gets passed intVo a new node.
    # we have to add to the length as well



  def dequeue(self):
      self.size -= 1
      # print('len after dequeue', self.len())
      return self.storage.pop()


  def len(self):
      return self.size


q = Queue()
q.enqueue(999)
q.enqueue(101)
q.enqueue(105)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# q.dequeue()
# print('length after all', q.len())
# print('size', q.size)
print('pop 999?', q.dequeue())
print('size', q.size)
print('pop 101?', q.dequeue())
print('size', q.size)
print('pop 105?', q.dequeue())
print('size', q.size)
print('pop 0?', q.dequeue())



