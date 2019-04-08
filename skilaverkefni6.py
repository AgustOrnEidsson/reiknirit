#Ágúst Örn Eiðsson
#Skilaverkefni 6

import re

#1 Heildi og flatarmál
def flatarmal_falls(fall, upp, down):
    if fall[0] != "-":
        fall = "+" + fall
    merki = []
    for x in fall:
        if x == "+" or x == "-":
            merki.append(x)
    fall_listi = re.split('[+-]', fall)git
    try:
        fall_listi.remove("")
    except:
        pass
    buid = []
    for x in fall_listi:
        if "x" in x:
            a= x.index("x")
            temp_listi1 = x[:a]
            temp_listi2 = x[a + 1:]
            if a == 0 and len(x) == 2:
                framan = str(1 / (int(x[a + 1]) + 1))
                veldi = str(int(x[a + 1]) + 1)
                buid.append(framan + "*(x)**" + veldi)
            elif a!= 0 and len(x) > 2:
                framan = str(int(x[:a]) / (int(x[a + 1]) + 1))
                veldi = str(int(x[a + 1]) + 1)
                buid.append(framan + "*(x)**" + veldi)
            elif a== 0 and len(x) == 1:
                buid.append("0.5*(x)**2")
            if len(temp_listi1) != 0 and len(temp_listi2) == 0:
                framan = str(int(x[:a]) / 2)
                buid.append(framan + "*(x)**2")
        else:
            temp_s = fall_listi.index(x)
            temp = fall_listi[temp_s]
            buid.append(str(temp) + "*(x)")

    buid_fall = ""
    for x in range(len(buid)):
        buid_fall += merki[x] + buid[x]
    listi = ["*", "(", ")"]
    buid2 = buid_fall
    for x in listi:
        buid2 = buid2.replace(x, "")
    if buid2[0] == "+":
        buid2 = buid2[1:]
    nytt_fall_a = buid_fall.replace("x", str(down))
    nytt_fall_b = buid_fall.replace("x",

fall = input("Sláðu inn fall f(x): ")
fall1 = input("Sláðu inn fall g(x): ")
upp = float(input("X efri:: "))
down = float(input("X neðri: ")) str(upp))
    flatarmal = round(abs(eval(nytt_fall_b) - eval(nytt_fall_a)), 5)
    return flatarmal

flat = flatarmal_falls(fall, upp, down)
flat2 = flatarmal_falls(fall1, upp, down)
print("Flatarmálið milli f(x) og g(x) er", abs(round(flat - flat2, 5)))



#2 Memoization
with open("triangle.txt", "r") as f:
    a = f.read()
    l = a.split("\n")

for x in range(len(l)):
    l[x] = l[x].split(" ")
    for i in range(len(l[x])):
        l[x][i] = int(l[x][i])

cache = {}

def maxPath(l, lina, index):
    summa = l[lina][index]
    key = str(index) + "," + str(lina)
    if key in cache:
        return list(cache[key].keys())[0]
    if len(l) == int(lina) + 2:
        gildi = summa + max(l[lina + 1][index + 1], l[lina + 1][index])
        cache[key] = {gildi: str(summa) + "," + str(max(l[lina + 1][index + 1], l[lina + 1][index]))}
        return gildi
    else:
        path1 = maxPath(l, lina + 1, index)
        path2 = maxPath(l, lina + 1, index + 1)
        gildi = summa + max(path1, path2)
        if path1 > path2:
            cache[key] = {gildi: str(l[lina][index]) + "," + cache[str(index) + "," + str(lina + 1)][path1]}
        elif path1 <= path2:
            cache[key] = {gildi: str(l[lina][index]) + "," + cache[str(index + 1) + "," + str(lina + 1)][path2]}

        return gildi


s = maxPath(l, 0, 0)
summa = 0
for x in cache.values():
    if s == list(x.keys())[0]:
        leid = x
        l = x[s].split(",")
        for x in l:
            summa += int(x)

print("Summa:", summa)

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
        if self.root:
           return self.root.preOrderPrint()
    def postOrderPrint(self):
        if self.root:
           return self.root.postOrderPrint()
    def delete(self):
        if self.root:
           return self.root.delete()

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
t.preOrderPrintN()
t.postOrderPrintN()

