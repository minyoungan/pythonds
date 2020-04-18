from test import testEqual

def buildTree():
    r = BinaryTree('a')
    insertLeft(r,'b')
    insertRight(r[1],'d')
    insertRight(r,'c')
    insertRight(r[2],'f')
    insertLeft(r[2],'e')
    return r

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def getRightChild(root):
    return root[2]

def getLeftChild(root):
    return root[1]

ttree = buildTree()
testEqual(getRootVal(getRightChild(ttree)),'c')
testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')
