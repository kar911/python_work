class Node:
    def __init__(self,data):
        self.data=data
        self.height=0
        self.leftc=None
        self.rightc=None

class AVLT:
    def __init__(self):
        self.root=None
        self.count=0

    def insert(self, data):
        newn = Node(data)
        if not self.root:
            self.root = newn
            self.count += 1
        else:
            self.inst(self.root,data)

    # def insertNode(self,data,node):
    #     if data < node.data:
    #         if node.leftc :
    #             self.insertNode(data,node.leftc)
    #         else:
    #             node.leftc=Node(data)
    #     else:
    #         if node.rightc:
    #             self.insertNode(data, node.rightc)
    #         else:
    #             node.rightc = Node(data)

    def inst(self,node,data):
        if node:
            if data < node.data:
                node.leftc=self.inst(node.leftc,data)
            if data > node.data:
                node.rightc=self.inst(node.rightc,data)
        node.height=max(self.cal_height(node.leftc),self.cal_height(node.rightc)) +1
        return self.settelViolation(data,node)

    def settelViolation(self,data,node):
        balance=self.cal_balance(node)
        if balance > 1 and data < node.leftc.data:
            print("LL heavy")
            return self.rro(node)
        if balance < -1 and data >node.rightc.data :
            print("RR heavy")
            return self.lro(node)
        if balance > 1 and data > node.leftc.data:
            print("LR heavy")
            node.leftc=self.lro(node.leftc)
            return self.rro(node)
        if balance < -1 and data < node.rightc.data :
            print("RL heavy")
            node.rightc=self.rro(node.rightc)
            return self.lro(node)
        return node

    def remove(self,data):
        if self.root:
            self.root=self.removen(data,self.root)
    def removen(self,data,node):
        if not node:
            return Node
        elif data > node.data:
            node.leftc=self.removen(data,node.rightc)
        elif data < node.data:
            node.rightc=self.removen(data,node .leftc)
            if not node.leftc and not node .rightc:
                print("node with no child ,to be removed...")
                del  node
                return None
            if not node.leftc:
                print("node with right child,to be removed...")
                temp = node.rightc
                del node
                return temp
            elif not node.rightc:
                print("node with left child,to be removed...")
                temp = node.leftc
                del node
                return temp
            print("removing node with two children...")
            temp = self.pred(node.leftc)
            node.data = temp.data
            node.leftc = self.removen(temp.data, node.leftc)
        if not node:
            return node
        node.height=max(self.cal_height(node.leftc),self.cal_height(node.rightc))+1
        balance=self.cal_balance(node)
        if balance > 1 and self.cal_balance(node.leftc)>=0:
            return self.rro(node)
        if balance > 1 and self.cal_balance(node.leftc)<0 :
            node.leftc=self.lro(node.leftc)
            return self.rro(node)
        if balance < -1 and self.cal_balance(node.rightc)<=0:
            return self.lro(node)
        if balance < -1 and self.cal_balance(node.rightc)>0:
            node.rightc=self.rro(node.rightc)
            return self.lro(node)
        return node

    def pred(self,node):
        if node.rightc:
            self.pred(node.rightc)
        return node


    def cal_height(self,node):
        if not node:
            return -1
        return node.height
    def cal_balance(self,node):
        if not node:
            return 0
        return self.cal_balance(node.leftc) - self.cal_balance(node.rightc)
    def rro(self,node):
        print("rotating right",node.data)
        tmpleft=node.leftc
        t=tmpleft.rightc
        tmpleft.rightc=node
        node.leftc=t
        node.height=max(self.cal_height(node.leftc),self.cal_height(node.rightc))+1
        tmpleft.height=max(self.cal_height(tmpleft.leftc),self.cal_height(tmpleft.rightc))+1
        return tmpleft

    def lro(self,node):
        print("rotating left",node.data)
        tmpright=node.rightc
        t=tmpright.leftc
        tmpright.leftc=node
        node.rightc=t
        node.height=max(self.cal_height(node.leftc),self.cal_height(node.rightc))+1
        tmpright.height=max(self.cal_height(tmpright.leftc),self.cal_height(tmpright.rightc))+1
        return tmpright

    def traversein(self):
        if self.root:
            self.travin(self.root)

    def travin(self, node):
        if node:
            if node.leftc:
                self.travin(node.leftc)
            print(f"{node.data} {node.height}")
            if node.rightc:
                self.travin(node.rightc)
        

    def traversepre(self):
        if self.root:
            self.travpre(self.root)

    def travpre(self, node):
        if node:
            print(f"{node.data}")
            if node.leftc:
                self.travpre(node.leftc)
            if node.rightc:
                self.travpre(node.rightc)

    def traversepost(self):
        if self.root:
            self.travpost(self.root)

    def travpost(self, node):
        if node:
            if node.leftc:
                self.travpost(node.leftc)
            if node.rightc:
                self.travpost(node.rightc)
            print(f"{node.data}")

avl =AVLT()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.traversein()