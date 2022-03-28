# structure is like None->11->12->13->14->15->16->122
#          the newly added is the self head
class DNode(object):

    def __init__(self,data,nxt=None,prev=None):
        self.data =data
        self.nxt=nxt
        self.prev=prev

class DoubleL(object):

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        self.posi=0
        self.Cdata=None

    def new(self,data):
        self.size=self.size+1
        newt=DNode(data)
        if self.head is None:
            self.head=newt
            self.head.nxt=None
            self.head.prev=None
        elif self.size == 2:
            self.head.nxt=newt
            newt.prev=self.head
            self.tail=newt
            newt.nxt=None
            self.posi=self.posi-1       # structure is like None->11->12->13->14->15->16->122
        else:                          # the posi value  is -1   -2  -3  -4  -5  -6  -7   -8
            self.tail.nxt=newt
            newt.prev=self.tail
            self.tail=newt
            newt.nxt=None
            self.posi=self.posi-1
    # def currpoint(self,Cdata):
    def trevfTail(self,step): # structure is like None->11->12->13->14->15->16->122
        if step >=self.size:
            step=self.size
        cn = self.tail # it teverse like               <----<----<----<-----<----<
        cp=self.posi
        while step > 0:
            print(cn.data)
            cn = cn.prev
            cp += 1
            step -=1
        self.posi=cp
    def trevTail(self):
        if self.tail:
            self.trevaTail(self.tail)
    def trevaTail(self,node):
        if node:
            print(node.data)
            self.trevaTail(node.prev)
        pass


    def trevfHead(self,step):# structure is like None->11->12->13->14->15->16->122
        if step >=self.size:
            step=self.size
        cp=self.posi# it teverse like                >---->---->---->----->---->
        cn=self.head#          the newly added is the self head
        while step >0:
            print(cn.data)
            cn=cn.nxt
            cp-=1
            step-=1
        self.posi = cp

        # def trevFHead(self, step):
        #     if self.head:
        #         self.trevfHead(step, self.head)
        #
        # def trevfHead(self, step, node):  # structure is like None->11->12->13->14->15->16->122
        #     if step != 0:
        #         if node:
        #             print(node.data)
        #             self.trevfHead(step - 1, node.nxt)
ll=DoubleL()
ll.new(212)
ll.new(11)
ll.new(12)
ll.new(13)
ll.new(14)
ll.new(15)
ll.new(16)
ll.new(122)
print(ll.size)
ll.trevfHead(9)

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.nx = None
#
# class LinkedL(object):
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def newstart(self, data):
#         self.size = self.size + 1
#         newNode = Node(data)
#         if not self.head:
#             self.head = newNode
#         else:
#             newNode.nx = self.head
#             self.head = newNode
#
#     def dropHead(self):
#         if self.head:
#             self.size = self.size - 1
#             CnewNode = self.head
#             self.head = CnewNode.nx
#         else:
#             print("its that was the last node")
#     def dropPoint(self,data):
#         if self.head is not None:
#             cur=self.head
#             prev=None
#             while cur.data != data:
#                 prev=cur
#                 cur=cur.nx
#             if prev == None:
#                 self.head =cur.nx
#             else:
#                 prev.nx = cur.nx
#         else:
#             "Linked List in Empty"
#     def insertanyWhere(self, data, pos=0):
#         if pos == 0:
#             self.newstart(data)
#         else:
#             self.size = self.size + 1
#             CNode = self.head
#             prev = None
#             newn = Node(data)
#             while pos > 0:
#                 prev = CNode
#                 CNode = CNode.nx
#                 pos=pos-1
#             if CNode is None:
#                 prev.nx=newn
#                 newn.nx=None
#             elif CNode is not None:
#                 prev.nx=newn
#                 newn.nx=CNode
#     def travese(self):
#         nwst=self.head
#         c=True
#         while c:
#             print(f"{nwst.data}")
#             nwst=nwst.nx
#             if nwst ==None:
#                 c=False
# l = LinkedL()
# l.newstart(11)
# l.newstart(12)
# l.newstart(13)
# l.newstart(14)
# l.newstart(15)
# l.newstart(16)
# print(l.size,"\n")
# l.dropPoint(13)
# l.insertanyWhere(133,3)
# l.travese()