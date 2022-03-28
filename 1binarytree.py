class Node:
    def __init__(self, data):
        self.data = data
        self.leftc = None
        self.rightc = None


class binaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        newn = Node(data)
        if not self.root:
            self.root = newn
            self.count += 1
        else:
            self.insN(data)

    def insN(self, data):
        node = self.root
        while 1:
            if data < node.data:
                if node.leftc:
                    node = node.leftc
                elif not node.leftc:
                    node.leftc = Node(data)
                    self.count += 1
                    break
            elif data > node.data:
                if node.rightc:
                    node = node.rightc
                elif not node.rightc:
                    node.rightc = Node(data)
                    self.count += 1
                    break
            else:
                print(f"can't insert duplicate rules!! at {self.count + 1} number")
                break

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
    def min(self):
        if not self.root:
            print("no data in tree")
        else:
            node = self.root
            while 1:
                if node.leftc:
                    node = node.leftc
                else:
                    print(f"{node.data}")
                    break
    def max(self):
        if not self.root:
            print("no data in tree")
        else:
            node = self.root
            while 1:
                if node.rightc:
                    node = node.rightc
                else:
                    print(f"{node.data}")
                    break

    def traversein(self):
        if self.root:
            self.travin(self.root)

    def travin(self, node):
        if node:
            if node.leftc:
                self.travin(node.leftc)
            print(f"{node.data}",end='')
            if node.rightc:
                self.travin(node.rightc)

    def traversepre(self):
        if self.root:
            self.travpre(self.root)

    def travpre(self, node):
        if node:
            print(f"{node.data}",end='')
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
            print(f"{node.data}",end='')

    def remove(self, data):
        if self.root:
            self.rem(data,self.root)

    # def remfirst(self, data,node):
    #     prvnode=self.root
    #     l=False
    #     r=False
    #     while 1:
    #         if node is not None:
    #             if node.data > data:
    #                 node=node.leftc
    #                 if l:
    #                     prvnode = prvnode.leftc
    #                     l = False
    #                 elif r:
    #                     prvnode = prvnode.rightc
    #                     r = False
    #                 l=True
    #             elif node.data < data:
    #                 node=node.rightc
    #                 if l:
    #                     prvnode=prvnode.leftc
    #                     l=False
    #                 elif r:
    #                     prvnode = prvnode.rightc
    #                     l = False
    #                 r=True
    #             elif node.data == data:
    #                 if not node.rightc and not node.leftc:
    #                     print("removing leaf node...")
    #                     del node
    #                     break
    #                 elif not node.leftc:
    #                     print("removing node with single right child...")
    #                     prvnode.rightc = node.rightc
    #                     del node
    #                     break
    #                 elif not node.rightc:
    #                     print("removing node with single left child...")
    #                     prvnode.leftc = node.leftc
    #                     del node
    #                     break
    #                 else:
    #                     print("removing node with two children...")
    #                     temp = self.predessor(node.leftc)
    #                     node.data = temp.data
    #                     node.leftc=self.rem(temp.data,node.leftc)
    #             else:
    #                 print("no element like given to delete..")
    #                 break

    def rem(self,data,node):
        if not node: #the next three if are for searching
            return node
        if data < node.data:
            node.leftc=self.rem(data,node.leftc)
        elif data > node.data:
            node.rightc=self.rem(data,node.rightc)
        else: # this is converting after the seaching
            if not node.rightc and not node.leftc:
                print("removing leaf node...")
                del node
                return None
            if not node.leftc:
                print("removing node with single right child...")
                temp=node.rightc
                del node
                return temp
            elif not node.rightc:
                print("removing node with single left child...")
                temp=node.leftc
                del node
                return temp
            print("removing node with two children...")
            temp=self.predessor(node.leftc)
            node.data=temp.data
            node.leftc=self.rem(temp.data,node.leftc)
        return node

    def predessor(self, node):
        c = node
        while 1:
            if c.rightc:
                c = node.rightc
            else:
                return node


d = binaryTree()
# d.insert(32)
# d.insert(10)
# d.insert(1)
# d.insert(19)
# d.insert(16)
d.insert(1)
d.insert(2)
d.insert(3)
d.insert(4)
d.insert(5)
d.insert(6)
d.insert(7)
d.traversein()
print("\n")
# print("d", d.count)
# d.remove(10)
d.traversepre()
print("\n")
d.traversepost()
