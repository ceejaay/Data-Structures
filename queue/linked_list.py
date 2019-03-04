
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node 

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node




class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


    def insert_tail(self, value):
        n = Node(value)
        self.tail.next_node = n
        self.tail = n
        # create new node set next node to none.
        # Take the last node. Set next node to the new node.

    def insert_head(self, value):
        # create a new node
        n = Node(value)
        # the new node get's it's next node set to the previous head node.
        n.next_node = self.head.next_node
        # then the head gets set to the new node
        self.head = n

    def delete_from_head(self):
        # the new head
        new_head = self.head.next_node
        # set what was previously the second element to the head
        self.head = new_node

    def delete_from_tail(self):
        pass



b = Node(2, None)
a = Node(1, b)
print(b.value)
print(b.next_node)
print(a.value)
print(a.next_node.value)

# print(b.next_node.value)

l = LinkedList(a, b)

print(l.head.value)


l.insert_head('a')

print(l.head.value)





