# Romika Chaudhary
# C0921918
# March 7, 2024

class Node:
    def __init__(self, data=None):
        #Each node stores data and reference to its left and right children
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    #Uses recursion for insertion, traversal and search

    def __init__(self):
        self.root = None

    def insert(self, data):
        #If the tree is empty, the new node becomes the root,
        #otherwise it is inserted recursively based on the value
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    #Traverse the binary search in preorder, inorder and postorder respectively
    def print_preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(root.data, end=" ")
            self.print_inorder(root.right)

    def print_postorder(self, root):
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root.data, end=" ")

    #Searches for a specific value in binary searcg tree
    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data, count=0):
        if node is None:
            return 0
        elif node.data == data:
            return count + 1
        elif data < node.data:
            return self._search_recursive(node.left, data, count + 1)
        else:
            return self._search_recursive(node.right, data, count + 1)

#Creating BST for Sequence A
tree_a = BinarySearchTree()
sequence_a = [1, 5, 4, 6, 7, 2, 3]
for num in sequence_a:
    tree_a.insert(num)

#Searching Sequence A tree for values 1, 4, 2
print("Searching Sequence A tree:")
print("1 found after", tree_a.search(1), "nodes visited")
print("4 found after", tree_a.search(4), "nodes visited")
print("2 found after", tree_a.search(2), "nodes visited")

#Creating BST for Sequence B
tree_b = BinarySearchTree()
sequence_b = [150, 125, 175, 166, 163, 123, 108, 116, 117, 184, 165, 137, 141, 111, 138, 122, 109, 194, 143, 178, 173, 139, 126, 170, 190, 140, 188, 120, 195, 113, 104, 193, 181, 185, 198, 103, 182, 136, 115, 191, 144, 145, 155, 153, 151, 112, 129, 199, 135, 146, 157, 176, 159, 196, 121, 105, 131, 154, 107, 110, 158, 187, 134, 132, 179, 133, 102, 172, 106, 177, 171, 156, 168, 161, 149, 124, 189, 167, 174, 147, 148, 197, 160, 130, 164, 152, 142, 162, 118, 186, 169, 127, 114, 192, 180, 101, 119, 128, 100]
for num in sequence_b:
    tree_b.insert(num)

#Searching Sequence B tree for values 42, 142, 102, 190
print("\nSearching Sequence B tree:")
print("42 found after", tree_b.search(42), "nodes visited")
print("142 found after", tree_b.search(142), "nodes visited")
print("102 found after", tree_b.search(102), "nodes visited")
print("190 found after", tree_b.search(190), "nodes visited")

#Traversing Sequence A tree
print("\nTraversing Sequence A tree:")
print("Pre-order:", end=" ")
tree_a.print_preorder(tree_a.root)
print("\nIn-order:", end=" ")
tree_a.print_inorder(tree_a.root)
print("\nPost-order:", end=" ")
tree_a.print_postorder(tree_a.root)

#Traversing Sequence B tree
print("\n\nTraversing Sequence B tree:")
print("Pre-order:", end=" ")
tree_b.print_preorder(tree_b.root)
print("\nIn-order:", end=" ")
tree_b.print_inorder(tree_b.root)
print("\nPost-order:", end=" ")
tree_b.print_postorder(tree_b.root)