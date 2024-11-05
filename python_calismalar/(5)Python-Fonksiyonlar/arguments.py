def changeName(n):
    n="ada"

name="yiğit"

changeName(name)
print(name) #buradan yiğit bilgisi gelir

def change(n):  #burada referance kopyalaması yapıyoruz.yani adresi gönderiliyo
    n[0]="istanbul"

sehirler=["ankara","izmir"]

n=sehirler[:] #slicing işlemi yaptık. burada adres kopyalaması yapmadık o yüzden n değerini ekrana yazdığımızda ["ankara","izmir"] değerleri yazıcak.dizi korunacak

change(sehirler)
print(sehirler) #burada dizi ["istanbul","izmir"] olarak gelir



def add(*params): #tuple olarak istediğimiz kadar parametre almak istiyorsak tek yıldız kullanıyoruz

    print(params)
    return sum((params))

print(add(10,20))
print(add(10,20,40,70))
print(add(10,20,45,48))


def displayUser(**args): #key value olarak parametre gönderkem istiyorsak ** kullanıyoruz
    print(type(args))
    for key,value in args.items():
        print(f"{key} is {value}")

displayUser(name="çınar",age=2,city="istanbul")
displayUser(name="ada",age=12,city="ankara",phone=123456)
displayUser(name="yiğit",age=22,city="denizli",phone=123456789,email="yiğit@gmail.com")



def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1",key2="value 2")