# Ek program likhiye jo dictionary me se duplicate keys hata de.
dic={"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3
}
d={}
for i in dic:
    d.update(dic)
print(d) 
    