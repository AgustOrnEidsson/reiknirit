#Skilaverkefni 2 – FORR3RR05DU

#1.	Sauðakóði er kóði sem er skrifaður á mannamáli. Þetta er gert svo hver sem er geti vitað hvað er verið að plana að gera.

'''
2.
Forritið byrja á því að að gera fall sem tekur við tölu sem við köllum n
ef sú tala er stærri en 0 þá kallar fallið á sig sjálft. Þegar það kallar aftur á sig þá er n = gamla n nema því er deilt með 2 og engnir aukastafir teknir með.
Skila svo tölu á endanum en þegar ég skila henni þá skila ég því með því að taka modulus af töluni.
'''


#3.
def summa(n):
    if n==0:
       return n
    else:
        return n*n+summa(n-1)


t=int(input("- "))
print(summa(t))



#4
def runa(n):
    if n==0:
        print(n)
    else:
        runa(n-1)
        print((n*(n+1))/2)

t=int(input("- "))
runa(t)


#5 laga
def summ(n):
  if n == 0:
    return n
  else:
    return (n%10) + summ(n//10)

t=int(input("- "))
print(summ(t))


#6
def sam(a,b):
    if a==b or b==0:
        return a
    else:
        return sam(b, a%b)

t1=int(input("- "))
t2=int(input("- "))
print(sam(t1,t2))

