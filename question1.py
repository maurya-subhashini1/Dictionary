# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa 
# jaaye jaise ki niche Expected result me diya gaya hain or jisski bhi keys same 
# hai unki values add ho jai.



dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dict4={}
# if i in dic1:
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
# print(dict4)
dic4={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i==j:
                a=dic1[i]+dic2[j]
                dic4[i]=a
# print(dict4)
dict4={}
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
for c in dic4:
    for d in dict4:
        if c==d:
            dict4[c]=dic4[d]
            break
print(dict4)

        