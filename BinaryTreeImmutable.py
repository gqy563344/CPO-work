class Node(object):
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def add(root, value):
    new_node = Node(value)
    if root is None:
        root = new_node
    else:
        q = [root]
    while True:
        pop_node = q.pop(0)
        if pop_node.left is None:
            pop_node.left = new_node
            return
        elif pop_node.right is None:
            pop_node.right = new_node
            return
        else:
            q.append(pop_node.left)
            q.append(pop_node.right)

def size(node):
    if node is None:
        return 0
    else:
        return size(node.right)+size(node.left)+1

def delete(root, value):

    if root is None:
        return False
    parent = get_parent(root,value)
    if parent:
        del_node = parent.left if parent.left.value == value else parent.right
        if del_node.left is None:
            if parent.left.value == value:
                parent.left = del_node.right
            else:
                parent.right = del_node.right
            del del_node
            return True
        elif del_node.right is None:
            if parent.left.value == value:
                parent.left = del_node.left
            else:
                parent.right = del_node.left
            del del_node
            return True
        else:  # left and right all are not None
            tmp_pre = del_node
            tmp_next = del_node.right
            if tmp_next.left is None:
                # replace
                tmp_pre.right = tmp_next.right
                tmp_next.left = del_node.left
                tmp_next.right = del_node.right
            else:
                while tmp_next.left:
                    tmp_pre = tmp_next
                    tmp_next = tmp_next.left
                # replace
                tmp_pre.left = tmp_next.right
                tmp_next.left = del_node.left
                tmp_next.right = del_node.right
            if parent.left.value == value:
                parent.left = tmp_next
            else:
                parent.right = tmp_next
            del del_node
            return True
    else:
        return False

def traverse(root):  # 层次遍历
    if root is None:
        return None
    q = [root]
    res = [root.value]
    while q != []:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            res.append(pop_node.left.value)

        if pop_node.right is not None:
            q.append(pop_node.right)
            res.append(pop_node.right.value)
    return res

def preorder(root):  # 先序遍历
    if root is None:
        return []
    result = [root.value]
    left_value = preorder(root.left)
    right_value = preorder(root.right)
    return result + left_value + right_value

def inorder(root):  # 中序序遍历
    if root is None:
        return []
    result = [root.value]
    left_value = inorder(root.left)
    right_value = inorder(root.right)
    return left_value + result + right_value

def postorder(root):  # 后序遍历
    if root is None:
        return []
    result = [root.value]
    left_value = postorder(root.left)
    right_value = postorder(root.right)
    return left_value + right_value + result

def to_list(root):
    r=[]
    if root is None:
        return r
    if root.value is None:
        return r
    stack=[root]
    while stack:
        temp=stack.pop(0)
        if temp.value is not None:
            r.append(temp.value)
        else:
            r.append(None)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
    return r


def get_parent(root, value):
    if root.value == value:
        return None
    tmp = [root]
    while tmp:
        pop_node = tmp.pop(0)
        if pop_node.left and pop_node.left.value == value:
            return pop_node
        if pop_node.right and pop_node.right.value == value:
            return pop_node
        if pop_node.left is not None:
            tmp.append(pop_node.left)
        if pop_node.right is not None:
            tmp.append(pop_node.right)
    return None

def find_max(root,maxl=0):
    if root is None:
        return maxl
    l_max=find_max(root.left)
    r_max=find_max(root.right)
    return max(l_max,r_max,root.value)

def mconcat(node1,node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node1 is None and node2 is None:
        return None
    node1.value = node1.value + node2.value
    node1.left = mconcat(node1.left, node2.left)
    node1.right = mconcat(node1.right, node2.right)
    return node1

def mempty():
    return None


def from_list(root, lst):
    lst_copy = lst.copy()
    j = 0
    if len(lst) == 0:
        root = None
        return
    elem = lst_copy.__getitem__(0)
    lst_copy.pop(0)
    root = Node(elem, None, None)
    queue = [root]
    temp = Node(None, None, None)
    for e in lst_copy:
        if j == 0:
            temp = queue.pop()
            temp.left = Node(e, None, None)
            queue.append(temp.left)
            j = 1
            continue
        if j == 1:
            temp.right = Node(e, None, None)
            queue.append(temp.right)
            j = 0
    return root



