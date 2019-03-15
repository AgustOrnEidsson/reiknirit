#ágúst örn
import re
jafna="-x2+5x-4"
fall_list=re.split("[+-]",jafna)
fall_list.remove("")
merki=[]

tel=0
#skoða allt þetta rugl
for x in jafna:
    if x=="+" or x=="-":
        merki.append(x)

for x in fall_list:
    if "x" in x:
        for i in x:
            if i=="x":
                la=x.index("x")
            if la!=0:
                fram=x[:la]
                fram2=str(int(fram)/2)
                if x[la+1:]=="":
                    veldi=str(2)
                else:
                    veldi=str(int(x[la+1:])+1)
                fall_list[tel]=fram2+"x"+veldi
            else:
                print("kall")
    else:
        fall_list[tel]=x+"x"
    tel+=1

print(fall_list)
print(merki)
