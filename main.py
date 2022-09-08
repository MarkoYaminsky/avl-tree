import AVLTree as avl

if __name__ == "__main__":
    avl_tree = avl.AVLTree()
    root = avl_tree.insert(None, 0)
    tree_values = [1, 2, 3, 4, 5, 6, 7]
    for number in tree_values:
        root = avl_tree.insert(root, number)
    avl_tree.postorder(root)