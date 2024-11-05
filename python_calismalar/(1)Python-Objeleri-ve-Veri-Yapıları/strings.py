name = "onur"
surname="karagoz"
age=21

greeting="my name is "+name+" "+surname+" and \nI am "+ str(age)+" years old"

print(greeting)
print(len(greeting))
print(greeting[45])
print(greeting[-1]) 

print(greeting[2:5]) #ikinci indexten başlayıp beşinci indexse kadar al demek

print(greeting[3:]) #üçüncü karakterden başla sona kadar al demek 

print(greeting[:15]) # en baştan al 15. karaktere kadar git demek

print(greeting[2:40:2]) #2. karakterden başla 40. karaktere kadar git ama her iki karakterde bir al
