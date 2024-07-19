# Python program to implement a binary search tree

# Class to represent a node in the BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Function to do inorder traversal of the BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def main():
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    # Print inorder traversal of the BST
    inorder(root)

if __name__ == "__main__":
    main()
