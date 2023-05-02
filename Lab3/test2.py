import unittest
from bst import BinarySearchTree


class BSTTestCase(unittest.TestCase):

    def setUp(self):
        """
        Executed before each test method.
        Before each test method, create a BST with some fixed key-values. 
        """
        self.bst = BinarySearchTree()
        self.bst.add(36, "Value for 36")
        self.bst.add(11, "Value for 11")
        self.bst.add(22, "Value for 22")
        self.bst.add(45, "Value for 45")
        self.bst.add(2, "Value for 2")
        self.bst.add(56, "Value for 56")
        self.bst.add(48, "Value for 48")
        self.bst.add(27, "Value for 27")

    def test_add(self):
        """
        tests for add
        """
        # Create an instance of BinarySearchTree
        bsTree = BinarySearchTree()

        # bsTree must be empty
        self.assertEqual(bsTree.size(), 0)

        # Add a key-value pair
        bsTree.add(18, "Value for 18")
        # Size of bsTree must be 1
        self.assertEqual(bsTree.size(), 1)

        # Add another key-value pair
        bsTree.add(10, "Value for 10")
        # Size of bsTree must be 2
        self.assertEqual(bsTree.size(), 2)

        # The added keys must exist.
        self.assertEqual(bsTree.search(18), "Value for 18")
        self.assertEqual(bsTree.search(10), "Value for 10")

    def test_inorder(self):
        """
        tests for inorder_walk
        """
        actual_output = self.bst.inorder_walk()
        expected_output = [2, 11, 22, 27, 36, 45, 48, 56]

        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Inorder traversal must return a different sequence
        self.assertListEqual(self.bst.inorder_walk(), [
                             2, 11, 22, 25, 27, 36, 45, 48, 56])

    def test_postorder(self):
        """
        tests for postorder_walk
        """
        actual_output = self.bst.postorder_walk()
        expected_output = [2, 27, 22, 11, 48, 56, 45, 36]

        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Postorder traversal must return a different sequence
        self.assertListEqual(self.bst.postorder_walk(), [
                             2, 25, 27, 22, 11, 48, 56, 45, 36])

    def test_preorder(self):
        """
        tests for preorder_walk
        """
        self.assertListEqual(self.bst.preorder_walk(), [
                             36, 11, 2, 22, 27, 45, 56, 48])

        # Add one node
        self.bst.add(25, "Value for 25")
        # Preorder traversal must return a different sequence
        self.assertListEqual(self.bst.preorder_walk(), [
                             36, 11, 2, 22, 27, 25, 45, 56, 48])

    def test_search(self):
        """
        tests for search
        """
        actual_output = self.bst.search(56)
        expected_output = "Value for 56"
        self.assertEqual(actual_output, expected_output)

        self.assertFalse(self.bst.search(90))

        self.bst.add(90, "Value for 90")
        self.assertEqual(self.bst.search(90), "Value for 90")

    def test_remove(self):
        """
        tests for remove
        """
        self.bst.remove(56)

        self.assertEqual(self.bst.size(), 7)
        self.assertListEqual(self.bst.inorder_walk(), [
                             2, 11, 22, 27, 36, 45, 48])
        self.assertListEqual(self.bst.preorder_walk(),
                             [36, 11, 2, 22, 27, 45, 48])

    def test_smallest(self):
        """
        tests for smallest
        """
        self.assertTupleEqual(self.bst.smallest(), (2, "Value for 2"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(4, "Value for 4")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the smallest key is 0.
        self.assertTupleEqual(self.bst.smallest(), (0, "Value for 0"))

    def test_largest(self):
        """
        tests for largest
        """
        self.assertTupleEqual(self.bst.largest(), (56, "Value for 56"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(59, "Value for 59")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the largest key is 54
        self.assertTupleEqual(self.bst.largest(), (59, "Value for 59"))


if __name__ == "__main__":
    unittest.main()
