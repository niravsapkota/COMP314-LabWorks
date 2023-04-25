import unittest
from main import insertionSort, mergeSort

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        input1=[7,6,9,1,11]
        output1=[1,6,7,9,11]

        input2=[689,700,1200,302,700]
        output2=[302,689,700,700,1200]

        input3=[10,9,8,7,6,5,4,3,2,1]
        output3=[1,2,3,4,5,6,7,8,9,10]

        test1=insertionSort(input1)
        test2=insertionSort(input2)
        test3=insertionSort(input3)

        self.assertListEqual(test1, output1)
        self.assertListEqual(test2, output2)
        self.assertListEqual(test3, output3)

    def test_merge_sort(self):
        input1=[7,6,9,1,11]
        output1=[1,6,7,9,11]

        input2=[689,700,1200,302,700]
        output2=[302,689,700,700,1200]

        input3=[10,9,8,7,6,5,4,3,2,1]
        output3=[1,2,3,4,5,6,7,8,9,10]

        test1=mergeSort(input1, 0, len(input1)-1)
        test2=mergeSort(input2, 0, len(input2)-1)
        test3=mergeSort(input3, 0, len(input3)-1)

        self.assertListEqual(test1, output1)
        self.assertListEqual(test2, output2)
        self.assertListEqual(test3, output3)


if __name__ == '__main__':
    unittest.main()