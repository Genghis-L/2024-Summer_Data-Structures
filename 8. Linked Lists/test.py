class Node:
    def __init__(self, value: int, next_node: "Node"):  # constructor
        self.value = value
        self.next = next_node


temp = Node(17, None)
temp = Node(23, temp)
temp = Node(97, temp)
my_list = Node(44, temp)

current = my_list
while current:
    print(current.value)
    current = current.next
