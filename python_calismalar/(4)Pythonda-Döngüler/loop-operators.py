#range
# for item in range(50,100,10): # range methodu burada 50 den başla 10 ar 10 ar 100 e kadar git
#     print(item)

# print(list(range(50,100,20)))




# enumerate
# greeting="hello there"

# for index,letter in enumerate(greeting):
#     print(f"index: {index} letter: {letter} ")




# zip
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

print(list(zip(list1,list2))) #burada listeleri eşleştirdik 1,a 2,b 3,c gibi

for item in zip(list1,list2):
    print(item)

for a,b in zip(list1,list2):
    print(a) #burada sadece 1,2,3,4,5 yazdırıcak