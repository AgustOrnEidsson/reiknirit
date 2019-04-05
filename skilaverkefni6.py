#Ágúst Örn Eiðsson
#Skilaverkefni 6

#1 Heildi og flatarmál


#2 Memoization
'''
lis=[]
f=open("yaaas.txt","r")
lis=(f.read().split("\n"))
for x in range(len(lis)):
    lis[x]=lis[x].split(" ")
summa=int(lis[0][0])
tmp=[int(lis[1][0]),int(lis[1][1])]
num=0
f.close()
def lala(l,t,s,n):
    n+=1
    s=int(s)+int(max(t))
    print(t)
    sta=l[n].index(str(max(t)))
    print(sta)
    t=[l[n+1][sta],l[n+1][sta+1]]
    print(s,sta)
    return lala(l,t,s,n)

print(lala(lis,tmp,summa,num))

'''
#3 Binary Search Tree

class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def preOrderPrintN(self):
        print(self.value)
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()

    def postOrderPrintN(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):



    def postOrderPrint(self):
        1==1

    def delete(self):
        1==1
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa

    def deleteTree(self):
        1==1
        # Þinn kóði hér

t = Tree()
t.insert(27)
t.insert(7)
t.insert(57)
t.insert(62)
t.insert(13)
t.insert(56)
t.insert(2)
print(t.preOrderPrint())

