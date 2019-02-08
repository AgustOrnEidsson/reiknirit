import string

#1 flæðirit er með í foldernum
def hanoi(n,a,b,c):
    if n==1:
        print("færum %s frá %s til %s"%(n,a,b))
    else:
        hanoi(n-1,a,c,b)
        print("færum %s frá %s til %s"%(n,a,b))
        hanoi(n-1,a,b,c)

hanoi(3,"a","b","c")

#2
#flækju stigið er (2^3)-1 3 er þá n-ið

'''
3.
    A) O(n) er lykkja sem keyrir jafn oft og gildið á n
    B) O(n^2) er lykkja sem er innan í lykkju
    C) O(log(n)) er 

'''

#4
#4 A er bullshæt
'''
staerd=2
def abc(n):
    listi=string.ascii_lowercase
    for x in range(len(listi)):
        for r in range(len(listi)):
            if x<r:
                for i in range(len(listi)):
                    if r<i:
                        print(listi[x],listi[r],listi[i])

abc(3)
'''
t=string.ascii_lowercase
def e(t,l,h):
    p=t[h]
    i=l-1
    for x in range(l,h):
        if t[x]<=p:
            i+=1
            tmp=t[x]
            t[x]=t[i]
            t[i]=tmp
    tmp=t[h]
    t[h]=t[i+1]
    t[i+1]=tmp
    return i+1

def q(t,l,h):
    if l<h:
        o=e(t,l,h)
        q(t,l,o-1)
        q(t,o+1,h)

q(t,0,len(t)-1)
print(t)

'''
#5
lis=[]
def rada(n):
    for x in n:
        if x<n:


print(rada(lis))
'''

#QuickSort
t=[5,2,7,8,4]
def e(t,l,h):
    p=t[h]
    i=l-1
    for x in range(l,h):
        if t[x]<=p:
            i+=1
            tmp=t[x]
            t[x]=t[i]
            t[i]=tmp
    tmp=t[h]
    t[h]=t[i+1]
    t[i+1]=tmp
    return i+1

def q(t,l,h):
    if l<h:
        o=e(t,l,h)
        q(t,l,o-1)
        q(t,o+1,h)

q(t,0,len(t)-1)
print(t)
