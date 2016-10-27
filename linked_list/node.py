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
        nodes_have_equal_values = self.elem == other.elem
        next_nodes_have_equal_values = self.next == other.next
        return nodes_have_equal_values and next_nodes_have_equal_values 
        

    def __repr__(self):
        str(self)
