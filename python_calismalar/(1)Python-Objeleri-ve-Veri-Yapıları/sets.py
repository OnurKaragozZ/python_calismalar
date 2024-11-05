fruits={ "orange","apple","banana"}

# print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape"])

print(fruits)

myList=[1,2,4,4,5,6,6]

print(set(myList)) #set ettiğimiz listelerdeki tekrarlanan elemanlar bir kez yazılır


#iki method da istediğimiz değeri silmek için kullanılıyor
fruits.remove("mango") 
fruits.discard("apple")
fruits.clear()

