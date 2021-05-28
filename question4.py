
# Dic1= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#   	3:{    
#          'A' : 'WELCOME',
#          'B' : 'To',
#          'C' : 'DHARAMSALA'
#         }
#     }
# Dic1.pop(3,('A'))
# print(Dic1)




#     thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)



dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
}
count=0
for i in dict1:
    value_count=(len(dict1[i]))
    count+=value_count
print(count)
