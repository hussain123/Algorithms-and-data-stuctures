#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
    curr1 = l1
    curr2 = l2
    resultNode = ListNode(None, None)
    remainder = 0
    divide = 0
   
    while curr1!=None or curr2!= None:
        result  = curr1.val + curr2.val +remainder
        
        remainder = result//10
        result = result%10
        resultNode.next = ListNode(remainder)
        resultNode= resultNode.next
        curr1 = curr1.next
        curr2 = curr2.next

    return resultNode  

if __name__=='__main__':
    node1 = ListNode(2)
    node1.next = ListNode(4,ListNode(3, None))
    node2 = ListNode(5, ListNode(6, ListNode(4, None)))
    addTwoNumbers(node1,node2)
    print(9%10)
