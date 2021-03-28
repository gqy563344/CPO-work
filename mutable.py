# encoding: utf-8
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # search
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # insert code
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # delete node
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print("无该关键字，删除失败")
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p

    # previous visit tree
    def pre_visit(self, node):
        if node is not None:
            print(node.data)
            self.pre_visit(node.lchild)
            self.pre_visit(node.rchild)

    # mid visit tree
    def mid_visit(self, node):
        if node is not None:
            self.mid_visit(node.lchild)
            print(node.data)
            self.mid_visit(node.rchild)

    # last visit tree
    def last_vist(self, node):
        if node is not None:
            self.last_vist(node.lchild)
            self.last_vist(node.rchild)
            print(node.data)


a = [1, 12, 13, 4, 15, 6, 17, 8, 9]
bst = BST(a)  # build tree


#print(a)
#bst.insert(18)
bst.delete(bst.root, 91)
# print()
# bst.mid_visit(bst.root)
# print("previous visit")
# bst.pre_visit(bst.root)
# print("middle visit")
# bst.mid_visit(bst.root)  
# print("last visit")
# bst.last_vist(bst.root)