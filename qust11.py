# Ek code likhiye jo dictionary ki 3 highest value print karaye.

my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
list1_key=[]
list2_key=[]


for i in range(3):
    max=0
    for x in my_dict:
        if max<my_dict[x]:
            max=my_dict[x]
            key=x
    list1_key.append(max)
    # list2_key.append(key)
    my_dict.pop(key)
# print(list2_key)
print(list1_key)


