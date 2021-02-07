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
    pass

def inorder(root):
    if root:
        
        inorder(root.leftNode)
        print(root.data)
        inorder(root.rightNode)
def inorder_without_recursion(root):
    pass
def RangeSumBst(root,low, high):
    #print(sum)
    if root is None:
        return 0
    value = root.data if low<= root.data <= high else 0
    return value + RangeSumBst(root.leftNode, low, high) +RangeSumBst(root.rightNode, low, high)
if __name__ == '__main__':

    root = None
    root =  insert(root, 10)
    #print(root.leftNode)
    root  = insert(root, 5)
    root  = insert(root, 15)
    root  = insert(root, 3)
    root  = insert(root, 7)
    root  = insert(root,18)
    print(RangeSumBst(root, 7,15))
    