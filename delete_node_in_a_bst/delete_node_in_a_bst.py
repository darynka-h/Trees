# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode {self.val=}, {self.left=}, {self.right=}"

    def __eq__(self, other: 'TreeNode') -> bool:
        return self.val == other.val and self.left == other.left and self.right == other.right


    def search_dfs(self, required_node):
        if not self:
            return []
        result = [self.val]
        stack = [self]
        while len(stack):
            probe = stack.pop()
            result.append(probe.val)
            # result.append(probe)

            if probe.val == required_node:
                return result[-2], probe
                # return stack[-1], probe

            if probe.left is not None and probe.left.val not in result:
                stack.append(probe)
                stack.append(probe.left)
                continue
            if probe.right is not None and probe.right.val not in result:
                stack.append(probe.right)
                continue

        return None


# =====1========
# n_3 = TreeNode(3, None, None)
# n_7 = TreeNode(7, None, None)
# n_8 = TreeNode(8, None, n_3)
# n_5 = TreeNode(5, None, n_7)
# n_4 = TreeNode(4, None, n_5)
# n_1 = TreeNode(1, n_8, n_4)

# prev, current = n_1.search_bfs(5)
# prev, current = n_1.search_dfs(5)
# print(prev)
# print(current)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def search_dfs(self, required_node):
        if not self:
            return []
        result = [self.val]
        stack = [self]
        while len(stack):
            probe = stack.pop()
            result.append(probe.val)
            # result.append(probe)

            if probe.val == required_node:
                return result[-2], probe
                # return stack[-1], probe

            if probe.left is not None and probe.left.val not in result:
                stack.append(probe)
                stack.append(probe.left)
                continue
            if probe.right is not None and probe.right.val not in result:
                stack.append(probe.right)
                continue

        return None


class Solution:

    def search_dfs(self, node, required_node):
        if not self:
            return []
        result = [node.val]
        stack = [node]
        while len(stack):
            probe = stack.pop()
            result.append(probe.val)
            # result.append(probe)

            if probe.val == required_node:
                return result[-2], probe
                # return stack[-1], probe

            if probe.left is not None and probe.left.val not in result:
                stack.append(probe)
                stack.append(probe.left)
                continue
            if probe.right is not None and probe.right.val not in result:
                stack.append(probe.right)
                continue

        return None

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.right is None and root.left is None and key == root.val:
            return None

        if key == 0 and root is not None:
            return root

        if self.search_dfs(root, key) is None:
            return root

        prev_el_val, element_to_del = self.search_dfs(root, key)
        prev_el = self.search_dfs(root, prev_el_val)[1]

        if element_to_del.left is None and element_to_del.right is None:
            if element_to_del != root:
                if prev_el.left == element_to_del:
                    prev_el.left = None
                else:
                    prev_el.right = None
            else:
                root = None

        elif element_to_del.left is None or element_to_del.right is None:
            child = None
            if element_to_del.left:
                child = element_to_del.left
            else:
                child = element_to_del.right

            if element_to_del != root:
                if prev_el.left == element_to_del:
                    prev_el.left = child
                else:
                    prev_el.right = child
            else:
                root = child

        else:
            inheritor = element_to_del.right
            inheritor_parent = element_to_del

            while inheritor.left:
                inheritor_parent = inheritor
                inheritor = inheritor.left

            if inheritor_parent != element_to_del:
                inheritor_parent.left = inheritor.right
            else:
                element_to_del.right = inheritor.right

            element_to_del.val = inheritor.val

        return root


def tree_by_levels(node):
    if not node:
        return []
    result = [node.val]
    queue = [node]
    probe = node
    while len(queue):
        if probe.left:
            queue.append(probe.left)
        if probe.right:
            queue.append(probe.right)
        if queue[0].left:
            result.append(queue[0].left.val)
        if queue[0].right:
            result.append(queue[0].right.val)
        # print(result)
        queue = queue[1:]
        if len(queue) >= 1:
            probe = queue[0]
    return result

# ====дерево з умови літкоду ===========
# n_2 = TreeNode(2, None, None)
# n_7 = TreeNode(7, None, None)
# n_4 = TreeNode(4, None, None)
# n_3 = TreeNode(3, n_2, n_4)
# n_6 = TreeNode(6, None, n_7)
# n_5 = TreeNode(5, n_3, n_6)


# ============= велике дерево ============
# n_11 = TreeNode(11, None, None)
# n_25 = TreeNode(25, None, None)
# n_31 = TreeNode(31, None, None)
# n_42 = TreeNode(42, None, None)
# n_73 = TreeNode(73, None, None)
# n_85 = TreeNode(85, None, None)

# n_23 = TreeNode(23, n_11, n_25)
# n_35 = TreeNode(35, n_31, n_42)
# n_80 = TreeNode(80, n_73, n_85)

# n_30 = TreeNode(30, n_23, n_35)
# n_70 = TreeNode(70, None, n_80)

# n_50 = TreeNode(50, n_30, n_70)

# sol = Solution()
# print(tree_by_levels(n_50))
# print(tree_by_levels(sol.deleteNode(n_50, 30)))
