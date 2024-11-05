# value types => string, number

x=5
y=25
x=y

y=10
print(x,y)
# burada y de yaptığımız değişiklik x i etkilemedi


#reference types => list

a=["apple","banana"]
b=["apple","banana"]

a=b
b[0]="grape"

print(a,b)
#burada b de yaptığımız değişiklik a yı etkiledi çünkü burada adres ataması yapılıyor
