from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None # initialize starting node
        self.end = None # initialize ending node
        
        if elements: # if elements is not none
            for e in elements: # loop through each element
                node = Node(e) # convert it into a node
                if not self.start: # if self.start is none
                    self.start = node # assign the node to it
                    #print(self.start)
                if self.end: # if self.end is not none
                    self.end.next = node # assign node to its 'next' pointer
                    #print(self.end)
                self.end = node # assign the node to self.end, since we want self.end to be the last e we looped through
        
    def __str__(self):
        return '{}'.format([i for i in self])

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count

    def __iter__(self):
        if self.start: # if the LinkedList object has some value
            current = self.start # assign the self.start node to our current working node
            if current.next: # if current has a 'next' pointer to another node (i.e. there is more than 1 element in the input)
                nxt = self.start.next # assignt its 'next' node to our nxt working node
            yield current.elem # return the element of the current working node, then pause
            while current.next: # if the current working node had a 'next' pointer
                yield current.next.elem # return the element of the 'next' pointer of the current working node
                current = nxt # we finished with the current node, let's assign the new current working node to be the next one
                nxt = current.next # and let's assign the NEW current working node's 'next' pointer to our nxt working variable
        

    def __getitem__(self, index):
        length = len(self)
        if index < 0 and abs(index) > length:
            raise IndexError
        if length == 0 or length <= index:
            raise IndexError
        if index >= 0:
            for ind,element in enumerate(self):
                if ind == index:
                    return element                  
        else: #negative indexing
            for ind,element in enumerate(self):
                if ind - length == index: #defining relationship between negative index and positive index
                    return element
            # for idx, element in self.elements: 
                # no idea how but gotta get the index + element somehow
                # if idx == index:
                    # return element

    def __add__(self, other):
        copy = LinkedList(self) # created copy so we don't overwrite anything
        for i in other:
            copy.append(i) # append function is niiiceeeee
        return copy

    def __iadd__(self, other): # += operation, same as __add__ except we do want to overwrite the original LL
        for i in other:
            self.append(i)
        return self

    def __eq__(self, other):
        if len(self) == 0 and len(other) == 0: # if we have two empty LL's
            return True
        if not (self and other): #if either aren't filled
            return False
        if len(self) != len(other): #if lengths aren't equal
            return False
        for i,j in zip(self, other): # create a zip structure to compare parallel lists
            if i != j:
                return False
        return True

    def append(self, elem):
        node = Node(elem)  # create Node of elem       
        if self.start: # if our LL object has at least one element
            self.end.next = node # we create a 'next' pointer for the self.end node, pointing to Node(elem)
            self.end = node # our new self.end is our new Node(elem)
        else: # if our LL is empty
            self.start = node #initialize self.start
            self.end = node #initialize self.end

    def count(self):
        return len(self)

    def pop(self, index=None):
        length = len(self)
        if index == None: # default pop
            if length == 0:
                raise IndexError 
            elif length == 1: # special case. default pop for single element list
                popped_off_element = self.start.elem
                self.start = None
                return popped_off_element
            else:
                index = length - 1 # set the index to the last item
        elif length <= index:
            raise IndexError
        elif index == 0: # special case, pop first element off the list
            popped_off_element = self.start.elem
            self.start = self.start.next # now LinkedList starts with the second node
            return popped_off_element
        
        current = self.start.next
        count = 1
        previous = self.start
        while current:
            if count == index:
                pop = current.elem
                previous.next = current.next
                return pop
            else:
                previous = current
                current = current.next
                count += 1