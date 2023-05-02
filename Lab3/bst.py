# Defining the structure of node of the BST
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    # Returns the number of nodes in tree
    def size(self):
        return self.count

    def add(self, key, value):
        node = Node(key, value)

        # If tree is empty
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                # For value less than the root
                if key < current.key:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left

                # For value higher than the root
                elif key > current.key:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                else:
                    current.value = value
                    break
        self.count += 1

    # Search to return value for the key
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    # Gives the smallest key-value pair
    def smallest(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.key, current.value)

    # Gives the largest key-value pair
    def largest(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return (current.key, current.value)

    def remove(self, key):
        parent = None
        current = self.root
        while current is not None:
            if key == current.key:
                if current.left is None and current.right is None:
                    # Case 1: Node has no children
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.left is None:
                    # Case 2a: Node has only right child
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    # Case 2b: Node has only left child
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    # Case 3: Node has two children
                    successor_parent = current
                    successor = current.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    if successor_parent != current:
                        successor_parent.left = successor.right
                        successor.right = current.right
                    if parent is None:
                        self.root = successor
                    elif parent.left == current:
                        parent.left = successor
                    else:
                        parent.right = successor
                    successor.left = current.left
                self.count -= 1
                return True
            elif key < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return False

    def inorder_walk(self):
        keys = []
        self._inorder_walk(self.root, keys)
        return keys

    def _inorder_walk(self, node, keys):
        if node:
            self._inorder_walk(node.left, keys)
            keys.append(node.key)
            self._inorder_walk(node.right, keys)

    def preorder_walk(self):
        keys = []
        self._preorder_walk(self.root, keys)
        return keys

    def _preorder_walk(self, node, keys):
        if node:
            keys.append(node.key)
            self._preorder_walk(node.left, keys)
            self._preorder_walk(node.right, keys)

    def postorder_walk(self):
        keys = []
        self._postorder_walk(self.root, keys)
        return keys

    def _postorder_walk(self, node, keys):
        if node:
            self._postorder_walk(node.left, keys)
            self._postorder_walk(node.right, keys)
            keys.append(node.key)
