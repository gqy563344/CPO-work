import unittest
from hypothesis import given
import hypothesis.strategies as st
from BinaryTreeImmutable import *

class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None),0)
        root1 = Node(3)
        root2 = Node(3,Node(5,Node(6)),Node(9))
        self.assertEqual(size(root1),1)
        self.assertEqual(size(root2),4)

    def test_findmax(self):
        root = Node(3,Node(5,Node(6)),Node(9))
        self.assertEqual(find_max(root),9)


    def test_delete(self):
        root = Node(3,Node(5,Node(6)),Node(9))
        self.assertEqual(delete(root,6),True)


    def test_add(self):
        root = Node(3)
        add(root,4)

        self.assertEqual(preorder(root),[3,4])

    def test_mempty(self):
        self.assertEqual(mempty(),None)

    def test_mcomcat(self):
        root1 = Node(3,Node(5, Node(6)),Node(9))
        root2 = Node(1,Node(2,Node(4)),Node(8))
        root3=mconcat(root1,root2)
        self.assertEqual(preorder(root3),[4,7,10,17])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,x):
        b=Node()
        self.assertEqual(to_list(from_list(b,x)), x)

    def test_preorder(self):
        root = Node(3,Node(6, Node(5)),Node(9))
        lst_pre = preorder(root)
        self.assertEqual(lst_pre, [3, 6, 5, 9])

    def test_inorder(self):
        root = Node(3, Node(6, Node(5)),Node(9))
        lst_in=inorder(root)
        self.assertEqual(lst_in , [5,6,3,9])

    def test_postorder(self):
        root = Node(3, Node(6, Node(5)), Node(9))
        lst_post = postorder(root)
        self.assertEqual(lst_post, [5, 6, 9, 3])

    def test_traverse(self):
        root = Node(3, Node(6, Node(5)), Node(9))
        res = traverse(root)
        self.assertEqual(res, [3, 6, 9, 5])

if __name__ == '__main__':
 unittest.main()