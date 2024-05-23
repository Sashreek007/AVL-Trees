from using_queue import Queue
class AvlNode:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None
        self.height=1

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)

def searching(rootnode,target):
    if rootnode.data is None:
        return "Doesn't exist"
    if rootnode.data == target:
        return "Found"
    elif rootnode.data>target:
        if rootnode.left is not None:
            return searching(rootnode.left,target)
        else:
            return "Not found" 
    elif rootnode.data<target:
        if rootnode.right is not None:
            return searching(rootnode.right,target)
        else:
            return "Not found"

def getHeight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightRotation(disbalancedNode):
    newRoot=disbalancedNode.left
    disbalancedNode.left=newRoot.right
    newRoot.right=disbalancedNode
    disbalancedNode.height= 1+ max(getHeight(disbalancedNode.left),getHeight(disbalancedNode.right))
    newRoot.height= 1+ max(getHeight(newRoot.left),getHeight(newRoot.right)) 
    return newRoot

def leftRotation(disbalancedNode):
    newRoot= disbalancedNode.right
    disbalancedNode.right=newRoot.left
    newRoot.left=disbalancedNode
    disbalancedNode.height= 1+ max(getHeight(disbalancedNode.left),getHeight(disbalancedNode.right)) 
    newRoot.height= 1+ max(getHeight(newRoot.left),getHeight(newRoot.right)) 
    return newRoot

def getBalance(rootnode):
    if not rootnode:
        return 0
    return getHeight(rootnode.left)-getHeight(rootnode.right)

def insert(rootnode,newnode):
    if not rootnode:
        return AvlNode(newnode)
    if newnode < rootnode.data:
        rootnode.left=insert(rootnode.left,newnode)
    else:
        rootnode.right=insert(rootnode.right,newnode)
    

    if rootnode is None:
        return rootnode
    
    rootnode.height=1+ max(getHeight(rootnode.left),getHeight(rootnode.right))
    balance= getBalance(rootnode)
    if balance >1 and newnode< rootnode.left.data:
        return rightRotation(rootnode)
    if balance >1 and newnode > rootnode.left.data:
        rootnode.left= leftRotation(rootnode.left)
        return rightRotation(rootnode)
    if balance < -1 and newnode > rootnode.right.data:
        return leftRotation(rootnode)
    if balance < -1 and newnode < rootnode.right.data:
        rootnode.right= rightRotation(rootnode.right)
        return leftRotation(rootnode)
    return rootnode


def minimum_value(rootnode):
    if rootnode is None or rootnode.left is None:
        return rootnode
    return minimum_value(rootnode.left)

def delete_node(rootnode,nodevalue):
    if not rootnode:
        return
    elif nodevalue < rootnode.data:
        rootnode.left= delete_node(rootnode.left,nodevalue)
    elif nodevalue> rootnode.data:
        rootnode.right= delete_node(rootnode.right,nodevalue)
    else:
        if rootnode.left is None:
            temp= rootnode.right
            rootnode=None
            return temp
        if rootnode.right is None:
            temp = rootnode.left
            rootnode=None
            return temp
        temp = minimum_value(rootnode.right)
        rootnode.data=temp.data
        rootnode.right = delete_node(rootnode.right,temp.data)
        rootnode.height=1+ max(getHeight(rootnode.left),getHeight(rootnode.right))
        balance= getBalance(rootnode)
        if balance >1 and nodevalue< rootnode.left.data:
            return rightRotation(rootnode)
        if balance >1 and nodevalue > rootnode.left.data:
            rootnode.left= leftRotation(rootnode.left)
            return rightRotation(rootnode)
        if balance < -1 and nodevalue > rootnode.right.data:
            return leftRotation(rootnode)
        if balance < -1 and nodevalue < rootnode.right.data:
            rootnode.right= rightRotation(rootnode.right)
            return leftRotation(rootnode)
    return rootnode
        
avl = AvlNode(50)
avl=insert(avl,40)
avl=insert(avl,65)
avl=insert(avl,60)
avl=insert(avl,70)
avl=insert(avl,75)
avl= delete_node(avl,50)

levelOrderTraversal(avl)





