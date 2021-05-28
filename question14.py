list1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

dict1={}
for i in list1:
    h=list1[i]
    for i in list1:
        a=list1[i]
        if h>a:
            dict1[i]=a
for i in list1:
    h=list1[i]
    for i in list1:
        a=list1[i]
        if h<a:
            dict1[i]=a
print(dict1)

