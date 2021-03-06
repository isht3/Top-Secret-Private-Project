"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

import sys
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if node.value < value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(node.right, value)
        else:
            if node.left == None:
                node.right = Node(value)
            else:
                self._add(node.left, value)

    def view(self):
        if self.root is not None:
            self._view(self.root)

    def _view(self, node):
        if node is not None:
            self._view(node.left)
            print(node.value)
            self._view(node.right)


class CheckSearch:
    def __init__(self):
        self.last_value = None

    def checkBalanced(self, node):
        if node is None:
            return True

        if not self.checkBalanced(node.left):
            return False

        if self.last_value is not None and node.value <= self.last_value:
            return False

        if not self.checkBalanced(node.right):
            return False

        self.last_value = node.value

        return True


class Test(unittest.TestCase):

    def test_check_if_balanced(self):
        node3 = Node(3)
        node1 = Node(1)
        node5 = Node(5)
        node2 = Node(2)
        node4 = Node(4)
        node6 = Node(6)

        node3.left = node1
        node3.right = node5
        node1.right = node2
        node5.left = node4
        node5.right = node6

        tree = BinTree()
        tree.root = node3

        search = CheckSearch()
        print(search.checkBalanced(tree.root))


if __name__ == '__main__':
    unittest.main()
