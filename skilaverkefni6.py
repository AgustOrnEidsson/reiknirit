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


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self,d):
        a=Node(d)
        if a.left:
            a.left.preOrderPrint()
        if a.right:
            a.right.preOrderPrint()
        print( a.value,"asd")

    def postOrderPrint(self):
        1==1
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa

    def delete(n):
        1==1
        # Þinn kóði hér. Endurkvæmt fall sem fer yfir í Node klasa

    def deleteTree(self):
        1==1
        # Þinn kóði hér

t = Tree()
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
t.preOrderPrint(root)
