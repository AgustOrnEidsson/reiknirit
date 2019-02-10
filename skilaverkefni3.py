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
#flækju stigið er O(2^3)-1 3 er þá n-ið

'''
3.
    A) O(n) er lykkja sem keyrir jafn oft og gildið á n
    B) O(n^2) er lykkja sem er innan í lykkju
    C) O(log(n)) virkar þannig að t.d. þú ert með bunka af blöðum með nöfnum á en þau eru ekki í stafrófsröð þá tekur það fyrsta nafnið á öllum blaðsíðunum og reður blaðsíðunum eftir þeim

'''

#4
'''
a)
    26!
__________
(26-n)!*n!

b)
O(2^n)
'''
t=string.ascii_lowercase
y =[]
def q(n,s="",r = 0):
    if n > 0:
        for x in range(r,len(t)):
            if n == 1:
                y.append(s+t[x])
            r+=1
            q(n-1,s+t[x],r)
            
lengd = int(input("Veldu lengd strengsins: "))
q(lengd)
print(y)
'''
#5
y.reverse()

def b(t,l,h):
    i =l-1
    for x in range(l,h):
        if t[x] <= t[h]:
            i+=1
            t[x],t[i]=t[i],t[x]
    t[i+1],t[h]=t[h],t[i+1]
    return i+1
    
def p(t,l,h):
    if l<h:
        k=b(t,l,h)
        p(t,l,k-1)
        p(t,k+1,h)
p(y,0,len(y)-1)
print(y)
