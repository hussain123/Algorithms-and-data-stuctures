class Node: 
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class BstNode:
    
    def __init__(self, data):
        self.leftNode = None
        self.rightNode = None
        self.data = data

def insert(root, data):
    if root is None: 
        return BstNode(data)
    else:
        if  data <= root.data:
                root.leftNode = insert(root.leftNode, data)
        else:
            root.rightNode = insert(root.rightNode, data)
    
    return root
def delete(root, key):

    if root.data == key:
        if root.leftNode is None and root.rightNode is None:

def inorder(root):
    if root:
        
        inorder(root.leftNode)
        print(root.data)
        inorder(root.rightNode)
def inorder_without_recursion(root):

    if root: 
        
if __name__ == '__main__':

    root = None
    root =  insert(root, 1)
    print(root.leftNode)
    root  = insert(root, 5)
    root  = insert(root, 10)
    root  = insert(root, 2)
    inorder(root)
    