# Ek code likhiye jo dictionary ki 3 highest value print karaye.
#  expect result:-['e','b','c']
my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
a=[]
i=0
while i<3:
    max_key=max(my_dict,key=my_dict.get)
    a.append(max_key)
    my_dict.pop(max_key)
    i=i+1
print(a)