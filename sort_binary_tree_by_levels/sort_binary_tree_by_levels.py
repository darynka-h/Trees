class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not node:
        return []
    result = [node.value]
    queue = [node]
    probe = node
    while len(queue):
        if probe.left:
            queue.append(probe.left)
        if probe.right:
            queue.append(probe.right)
        if queue[0].left:
            result.append(queue[0].left.value)
        if queue[0].right:
            result.append(queue[0].right.value)
        # print(result)
        queue = queue[1:]
        if len(queue) >= 1:
            probe = queue[0]
    return result

# =====1========
# n_3 = Node(None, None, 3)
# n_7 = Node(None, None, 7)
# n_8 = Node(None, n_3, 8)
# n_5 = Node(None, n_7, 5)
# n_4 = Node(None, n_5, 4)
# n_1 = Node(n_8, n_4, 1)


# =====2========
    # листки
# n_1 = Node(None, None, 1)
# n_3 = Node(None, None, 3)
# n_4 = Node(None, None, 4)
# n_5 = Node(None, None, 5)

# n_8 = Node(n_1, n_3, 8)
# n_9 = Node(n_4, n_5, 9)

# n_2 = Node(n_8, n_9, 2)
# print(tree_by_levels(n_2))
