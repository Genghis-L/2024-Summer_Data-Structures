class Node:
    def __init__(self, element, next=None):
        self._element = element
        self._next = next

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insertAtFirst(self, element):
        new_node = Node(element, self._head)
        self._head = new_node

    def rearrange_even_odd(self):
        if self._head is None:
            return

        even_head = even_tail = None
        odd_head = odd_tail = None
        curr = self._head

        while curr:
            if curr._element % 2 == 0:  # even node
                if not even_head:
                    even_head = even_tail = curr
                else:
                    even_tail._next = curr
                    even_tail = curr
            else:  # odd node
                if not odd_head:
                    odd_head = odd_tail = curr
                else:
                    odd_tail._next = curr
                    odd_tail = curr
            curr = curr._next

        # Connect even and odd lists
        if even_tail:
            even_tail._next = odd_head
        else:
            even_head = odd_head

        if odd_tail:
            odd_tail._next = None

        self._head = even_head

    def __str__(self):
        result = "Head-->"
        current = self._head
        while current:
            result += str(current._element) + "-->"
            current = current._next
        result += "None"
        return result

# Example usage
sll = SinglyLinkedList()
sll.insertAtFirst(8)
sll.insertAtFirst(7)
sll.insertAtFirst(6)
sll.insertAtFirst(5)
sll.insertAtFirst(4)
sll.insertAtFirst(3)
sll.insertAtFirst(2)
sll.insertAtFirst(1)
print(sll)  # Before rearranging
sll.rearrange_even_odd()
print(sll)  # After rearranging
