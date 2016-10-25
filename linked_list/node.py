class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        # a = self.next.elem
        if self.next:
            string = "Node({}) > Node({})".format(self.elem, self.next.elem)
        else:
            string = "Node({}) > /".format(self.elem)
            
        return string
        
    # need to return something like "Node(9) > /"
    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        pass
