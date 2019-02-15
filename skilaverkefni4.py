#Ágúst Örn Eiðsson
#Reiknirit - Skilaverkefni 4

#2
'''
listi=[8,5,3,7,1,9,2,6]

def linear(l,t):
    if len(l)==0:
        return -1
    else:
        tel=-1
        for x in l:
            tel+=1
            if x==t:
                return "Talan",t,"er í sæti",tel
        return "Talan",t,"er ekki í listanum"

t=int(input("Sláðu inn tölu til að finna: "))

print(linear(listi,t))
'''

#3
'''
klara þetta seinna
listi=[1,2,3,4,5,6,7,8,9]

def binary(l,t,low,high):
    if len(l)==0:
        return -1
    else:
        p=len(l)//2
        if t<p:
            return "Bjælir"
        elif t==p:
            return binary(l)
        else:
            return "Talan",t,"er í sæti",p


t=int(input("Sláðu inn tölu til að finna: "))

print(binary(listi,t,0,len(listi)))
'''

#4

#5
listinn=[2,3,4,5,6,7,8,9,10]
#def rada(l,t):



#6
class node:
    def __init__(self,v):
        self.value=v
        self.left=None
        self.right=None

    def insert(self,d):
        if self.value==d:
            return False
        elif self.value>d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left=node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right=node(d)
                return True
    def find(self,d):
        if self.value==d:
            return True
        elif self.value>d:
            if self.left:
                return self.left.find(d)
            else:
                return False
        else:
            if self.right:
                return self.right.find(d)
            else:
                return False

class tree:
    def __init__(self):
        self.root=None

    def insert(self,d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root=node(d)
            return True
    def find(self,d):
        if self.root:
            return self.root.find(d)
        else:
            return False


t=tree()
print(t.insert(6))
print(t.insert(2))
print(t.insert(3))
print(t.insert(7))
print(t.find(3))
print(t.find(4))
print(t.find(6))
