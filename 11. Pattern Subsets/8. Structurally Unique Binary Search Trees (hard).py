class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_recursive(1, n)


def find_unique_trees_recursive(start, end):
    result = []
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end = 1, this means we shou
    # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
    # both of these should return 'None' for the left and the right child
    if start > end:
        result.append(None)
        return result

    for i in range(start, end+1):
        # making 'i' the root of the tree
        left_subtrees = find_unique_trees_recursive(start, i - 1)
        right_subtrees = find_unique_trees_recursive(i + 1, end)
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()