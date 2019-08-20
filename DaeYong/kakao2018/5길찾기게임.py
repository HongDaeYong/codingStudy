import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, x, y, i):
        self.n, self.x, self.y, self.used = i, x, y, False
        self.parent = self.left = self.right = None


class Tree:
    def __init__(self, nodes):
        self.root = nodes[0]
        for node in nodes[1:]:
            self._insert(node)

    def _insert(self, node):
        tmp_node = self.root
        while node.parent is None:
            if node.x < tmp_node.x:
                if tmp_node.left is None:
                    tmp_node.left = node
                    node.parent = tmp_node
                else:
                    tmp_node = tmp_node.left
            elif tmp_node.x < node.x:
                if tmp_node.right is None:
                    tmp_node.right = node
                    node.parent = tmp_node
                else:
                    tmp_node = tmp_node.right


def solution(nodeinfo):
    preorder_circulation = []
    postorder_circulation = []

    nodeinfo = [Node(coord[0], coord[1], i+1) for i, coord in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda a: a.y, reverse=True)

    tree = Tree(nodeinfo)

    def preord_circ(node):
        nonlocal preorder_circulation
        preorder_circulation.append(node.n)
        if node.left is not None:
            preord_circ(node.left)
        if node.right is not None:
            preord_circ(node.right)

    preord_circ(tree.root)

    stack = []
    tmp = tree.root
    stack.append(tmp)
    while tmp.left is not None:
        tmp = tmp.left
        stack.append(tmp)
    if tmp.right is not None:
        tmp = tmp.right
        stack.append(tmp)
    postorder_circulation.append(stack.pop().n)
    tmp.used = True

    while len(stack) != 0:
        tmp = stack.pop()
        if tmp.left is not None and not tmp.left.used:
            stack.append(tmp)
            stack.append(tmp.left)
        elif tmp.right is not None and not tmp.right.used:
            stack.append(tmp)
            stack.append(tmp.right)
        else:
            postorder_circulation.append(tmp.n)
            tmp.used = True
    return [preorder_circulation, postorder_circulation]


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(nodeinfo))

