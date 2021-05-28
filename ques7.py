x=[
    {"first":"1"}, 
    {"second": "2"}, 
    {"third": "1"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}
]
a=[]
for i in range(x):
    for f in x:
        if (x[i][f])not in a :
            a.append([i][f])
    print(a)

