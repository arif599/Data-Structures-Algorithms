class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, data):  
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
         
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    # data == current.data
                    break


def preorder(root):
    # root, left, right
    if root == None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right) 

def inorder(root):
    # left, root, right
    if root == None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right) 


def postorder(root):
    # left, right, root
    if root == None:
        return

    postorder(root.left)
    postorder(root.right) 
    print(root.data)

def preorderStack(root):
    stack = [root]

    while stack:
        current = stack.pop()
    
        print(current.data)
        if current.right: 
            stack.append(current.right)
        if current.left: 
            stack.append(current.left)

def inorderStack(root):
    stack = []
    current = root

    while stack or current:
        if current: 
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.data)
            current = current.right

def levelorder(root):
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        print(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

tree = BinarySearchTree()
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(2)
tree.insert(18)
tree.insert(12)
tree.insert(20)

print("PREORDER RECURSIVE:")
preorder(tree.root)
print("INORDER RECURSIVE:")
inorder(tree.root)
print("POSTORDER RECURSIVE:")
postorder(tree.root)

print("PREORDER STACK:")
preorderStack(tree.root)
print("INORDER STACK:")
inorderStack(tree.root)

print("LEVEL ORDER:")
levelorder(tree.root)




