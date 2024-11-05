#global scope
x="global x"

def function():
    #local scope
    x="local x"  #eğer burada x değerini tanımlamazsak aşağıda function() u çağırdığımızda orada da global x değeri gelicek 
    print(x)

function() #buradan local x değeri gelir
print(x) #buradam global x değeri gelir


#######################


#global
name="çınar"

def changeName(new_name):
    #local
    name=new_name
    print(name)

changeName("onur") #burada onur değerini verir
print(name) # burada çınar değerini verir


#######################

name="global string"

def greeting():
    name="çınar"

    def hello():
        print("hello "+name) #buradaki name in globali name="çınar" olan name dir

    hello()

greeting() #hello çınar yazdırır

#######################


x=50

def test(x):
    print(f"x: {x}")

    x=100
    print(f"changed x to {x}")

test(x)

#eğer dışarıdaki x bilgisini fonksiyonun içinde de değiştirmek istiyorsanız bu şekil bir kullanım yapmanız gerekir

x=50

def test():
    global x
    print(f"x: {x}")

    x=100
    print(f"changed x to {x}")

test()