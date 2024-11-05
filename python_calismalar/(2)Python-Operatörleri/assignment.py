# x=5
# y=10
# z=20

x,y,z=5,10,20

# x,y=y,x burada x in içine y,y nin içine x in değerini atadık


x+=5 # x=x+5 
x-=5 # x=x-5 
x*=5 # x=x*5
x/=5 # x=x/5
x%=5 # x=x%5
x//=5 # x=x//5 tam bölme örnek:3.2 çıkarsa 3 alınır
x**=5 # x=x**5 üs alma



values=1,2,3,4,5 #tuple liste
print(values)
print(type(values))

x,y,*z=values #burada 1 x e,2 y ye , geri kalanlar da liste halinde z ye gider yani z=[3,4,5]

print(x,y,z[1]) 
print(x,y,z) 

