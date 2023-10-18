class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printing(root):
    if root==None:
        return
    printing(root.right)
    printing(root.left)
    printing(root)
root=node(1)
root.right=node(2)
root.left=node(3)
root.left.right=node(4)
root.left.left=node(5)

q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.data)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)









    
