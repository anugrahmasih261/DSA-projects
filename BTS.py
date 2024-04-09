class TreeNode:  # Define a class representing a node in the Binary Search Tree (BST).
    def __init__(self, key):  # Constructor method to initialize a node with a key.
        self.key = key  # Assign the key value to the node.
        self.left = None  # Initialize the left child pointer to None.
        self.right = None  # Initialize the right child pointer to None.

class BST:  # Define a class representing the Binary Search Tree (BST).
    def __init__(self):  # Constructor method to initialize an empty BST.
        self.root = None  # Initialize the root of the BST to None.

    def insert(self, key):  # Method to insert a new key into the BST.
        self.root = self._insert_recursive(self.root, key)  # Call the recursive insertion method.

    def _insert_recursive(self, root, key):  # Recursive helper method for inserting a key into the BST.
        if root is None:  # If the current node is None (i.e., the tree is empty or a leaf node).
            return TreeNode(key)  # Create a new node with the given key value.

        if key < root.key:  # If the key is less than the key of the current node.
            root.left = self._insert_recursive(root.left, key)  # Recursively insert into the left subtree.
        elif key > root.key:  # If the key is greater than the key of the current node.
            root.right = self._insert_recursive(root.right, key)  # Recursively insert into the right subtree.
        
        return root  # Return the current node after insertion.

    def search(self, key):  # Method to search for a key in the BST.
        return self._search_recursive(self.root, key)  # Call the recursive search method.

    def _search_recursive(self, root, key):  # Recursive helper method for searching a key in the BST.
        if root is None or root.key == key:  # If the current node is None or contains the key.
            return root  # Return the current node.

        if key < root.key:  # If the key is less than the key of the current node.
            return self._search_recursive(root.left, key)  # Recursively search in the left subtree.
        else:  # If the key is greater than the key of the current node.
            return self._search_recursive(root.right, key)  # Recursively search in the right subtree.

# Example usage:
bst = BST()  # Create an instance of the Binary Search Tree (BST).
bst.insert(50)  # Insert keys into the BST.
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

search_key = int(input("Enter the key to search: "))  # Ask the user for a key to search.
result = bst.search(search_key)  # Search for the key in the BST.

if result:  # If the key is found in the BST.
    print(search_key,"Key found in BST at ", i)
else:  # If the key is not found in the BST.
    print("Key not found in BST")


'''
Time Complexity:

Insertion: O(log n) on average, where n is the number of nodes
in the BST. However, in the worst case, it can be O(n) 
if the tree becomes unbalanced. Search: O(log n) on average,
where n is the number of nodes in the BST. In the worst case,
 it can be O(n) if the tree becomes unbalanced. Space Complexity:

The space complexity of a BST is O(n), where n is the number of nodes in the tree, due to the space required to store the nodes.
'''
