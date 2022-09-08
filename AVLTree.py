class AVLTree:
    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.val:
            node.left = self.insert(node.left, key)
        elif key > node.val:
            node.right = self.insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                node = self.rotate_right(node)
            else:
                node = self.rotate_left_right(node)
        elif balance < -1:
            if self.get_balance(node.right) <= 0:
                node = self.rotate_left(node)
            else:
                node = self.rotate_right_left(node)

        return node

    def rotate_right(self, node):
        left_temp = node.left
        node.left = left_temp.right
        left_temp.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_temp.height = 1 + max(self.get_height(left_temp.left), self.get_height(left_temp.right))

        return left_temp

    def rotate_left(self, node):
        right_temp = node.right
        node.right = right_temp.left
        right_temp.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_temp.height = 1 + max(self.get_height(right_temp.left), self.get_height(right_temp.right))

        return right_temp

    def rotate_left_right(self, node):
        node.left = self.rotate_left(node.left)

        return self.rotate_right(node)

    def rotate_right_left(self, node):
        node.right = self.rotate_right(node.right)

        return self.rotate_left(node)

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    @staticmethod
    def get_height(node):
        if not node:
            return -1

        return node.height


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.height = 0
        self.left = None
        self.right = None