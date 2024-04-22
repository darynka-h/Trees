class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node({self.data=}, {self.left=}, {self.right=})"


def pre_order(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.data]
    left_in = pre_order(node.left)
    right_in = pre_order(node.right)
    return [node.data] + left_in + right_in


def in_order(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.data]
    left_in = in_order(node.left)
    right_in = in_order(node.right)
    return left_in + [node.data] + right_in


def post_order(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.data]
    left_in = post_order(node.left)
    right_in = post_order(node.right)
    return left_in + right_in + [node.data]

# b = Node("B")
# c = Node("C")
# a = Node("A")
# a.left = b
# a.right = c


# n_4 = Node(4)
# n_5 = Node(5)
# n_2 = Node(2)
# n_2.left = n_4
# n_2.right = n_5
# n_1 = Node(1)
# n_1.left = n_2

# n_6 = Node(6)
# n_7 = Node(7)
# n_3 = Node(3)
# n_3.left = n_6
# n_3.right = n_7

# n_1.right = n_3

# ========ланцюжок
c_ = Node(3)
b_ = Node(2)
b_.left = c_
a_ = Node(1)
a_.left = b_
# print(in_order(n_1))
# print(pre_order(n_1))
# print(post_order(n_1))
print(pre_order(a_))