class Node:
    """
    Node class to keep track of key and pointers
    """

    def __init__(self, key, left = None, right = None):
        self.left = left
        self.right = right
        self.key = key

"""
To test Bintree you can use simple numbers and print them in inorder, preorder and postorder and see if it's correct
"""

class Bintree:
    """
    Bintree class that contains methods for creating and handling the binomial tree data structure
    """

    def __init__(self):
        """
        Creates Bintree object with root none
        """

        self.root = None

    def __contains__(self,key):
        """
        Method to check if binomial tree contains certain value
        Paramters: Key you want to check if it contains
        Returns: True if key is in tree, False otherwise
        """

        return finns(self.root, key)
    
    def put(self, newkey):
        """
        Method to sort new key into tree
        Paramters: New key to add to tree
        Returns: New tree root
        """

        self.root = putta(self.root, newkey)

    def write(self):
        """
        Method to write tree contents inorder
        Parameters: None
        Returns: None
        """

        skriv(self.root)
        print("\n")

    def writepostorder(self):
        """
        Method to write tree contents postorder
        Parameters: None
        Returns: None
        """

        skrivpostorder(self.root)
        print("\n")
    
    def writepreorder(self):
        """
        Method to write tree contents preorder
        Parameters: None
        Returns: None
        """

        skrivpreorder(self.root)
        print("\n")

COUNT = [10]
def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.key)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
 
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
 

def putta(root, newkey):
    """
    Function that puts new values into tree recursively
    Parameters: root bintree object, new key to put into tree
    Returns: New root
    """
    
    if root == None:
        return Node(newkey)
    
    else:
        if newkey > root.key:
            if root.right == None:
                root.right = Node(newkey)
            
            else:
                putta(root.right, newkey)
        
        else:
            if root.left == None:
                root.left = Node(newkey)
            
            else:
                putta(root.left, newkey)
        
        return root

def finns(root, searched):
    """
    Function that checks if searched value is in tree recursively
    Parameters: root bintree object, value to search for
    Returns: True if key exists in tree and False otherwise
    """

    if root == None:
        #print("1")
        return False
    
    #print(root.key)
    #print(searched)
    
    if searched == root.key:
        #print("2")
        return True
    
    if searched > root.key:
        #print("3")
        return finns(root.right, searched)
    
    if searched < root.key:
        #print("4")
        return finns(root.left, searched)
   
    else:
        raise ValueError('An error has occured')
    
    
def skriv(root):
    """
    Function to write tree contents inorder
    Parameters: None
    Returns: None
    """

    if root is not None:
        skriv(root.left)
        print(root.key)
        skriv(root.right)

def skrivpostorder(root):
    """
    Function to write tree contents postorder
    Parameters: None
    Returns: None
    """

    if root is not None:
        skrivpostorder(root.left)
        skrivpostorder(root.right)
        print(root.key)

def skrivpreorder(root):
    """
    Function to write tree contents preorder
    Parameters: None
    Returns: None
    """

    if root is not None:
        print(root.key)
        skrivpreorder(root.left)
        skrivpreorder(root.right)