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

#3

#4
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
3.
    A) O(n) er lykkja sem keyrir jafn oft og gildið á n
    B) O(n^2) er lykkja sem er innan í lykkju
    C) O(log(n)) er 

'''
#flækju stig (2^n)-1

#5
lis=[]
def rada(n):
    for x in n:
        if x<n:


print(rada(lis))
