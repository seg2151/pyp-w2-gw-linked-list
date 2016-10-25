from .interface import AbstractLinkedList


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        pass

    def count(self):
        pass

    def pop(self, index=None):
        length = len(self)
        if length == 0 or index > length:
            raise IndexError
        else:
            # pop it and return the popped element
