list=[1,2,3]
tuple=(1,"iki",3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

list=["ali","veli"]
tuple=("damla","ayşe") 

list[0]="ahmet"
tuple[0]="deniz" #eğer böyle bir atama yaparsak "'tuple' object does not support item assignment" hatasını alırız tuple a eleman atandıktan sonra değiştirilemez.

names=("onur","mustafa","deniz") + tuple # iki tane tuple birleştirilebilir

print(names)

print(list)
print(tuple)