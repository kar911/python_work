class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

            # A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


    # Driver program to test the above functions


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current

# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r, Node(30))
insert(r, Node(21))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
inorder(r)


 def minValueNode(node):
     current = node

     # loop down to find the leftmost leaf
     while (current.left is not None):
         current = current.left

     return current


 # Given a binary search tree and a key, this function
 # delete the key and returns the new root
 def deleteNode(root, key):
     # Base Case
     if root is None:
         return root

         # If the key to be deleted is smaller than the root's
     # key then it lies in  left subtree
     if key < root.key:
         root.left = deleteNode(root.left, key)

         # If the kye to be delete is greater than the root's key
     # then it lies in right subtree
     elif (key > root.key):
         root.right = deleteNode(root.right, key)

         # If key is same as root's key, then this is the node
     # to be deleted
     else:

         # Node with only one child or no child
         if root.left is None:
             temp = root.right
             root = None
             return temp

         elif root.right is None:
             temp = root.left
             root = None
             return temp

             # Node with two children: Get the inorder successor
         # (smallest in the right subtree)
         temp = minValueNode(root.right)

         # Copy the inorder successor's content to this node
         root.key = temp.key

         # Delete the inorder successor
         root.right = deleteNode(root.right, temp.key)

     return root
