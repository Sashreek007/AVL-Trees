from using_queue import Queue
class AvlNode:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None
        self.height=1
    

def insert(rootnode,value):
    if rootnode.data is None:
        rootnode.data = value
    elif value<=rootnode.data:
        if rootnode.left is None:
            rootnode.left = AvlNode(value)
        else:
            insert(rootnode.left,value)
    elif value >rootnode.data:
        if rootnode.right is None:
            rootnode.right = AvlNode(value)
        else:
            insert(rootnode.right,value)
    return "successful"

def LevelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        custom_queue=Queue()
        custom_queue.enqueue(rootnode)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                custom_queue.enqueue(root.value.left)
            if root.value.right is not None:
                custom_queue.enqueue(root.value.right)

def searching(rootnode,target):
    if rootnode is None:
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
            return insert(rootnode.right,target)
        else:
            return "Not found"

    
avl = AvlNode(None)
print(insert(avl,70))
insert(avl,60)
insert(avl,80)
LevelOrderTraversal(avl)
print(searching(avl,10))


