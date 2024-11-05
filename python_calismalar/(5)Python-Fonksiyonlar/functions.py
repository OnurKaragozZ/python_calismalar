# def sayHello(name="user"):
#     print(f"hello {name}")

# sayHello("onur")
# sayHello("çınar")
# sayHello()




# def sayHello(name="user"):
#     return "hello "+name

# msg=sayHello("onur")
# print(msg)





# def total(num1,num2):
#     return num1+num2

# result=total(10,20)
# print(result)






def yasHesapla(dogumYili):
  return  2024-dogumYili

age=yasHesapla(2003)
print(age)



def EmekliligeKacYilKaldi(dogumYili,isim):
   """
   DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
   INPUT: Doğumyılı
   OUTPUT: Hesaplanan yıl bilgisi
   """
   yas=yasHesapla(dogumYili)
   emeklilik=65-yas

   if emeklilik>0:
      print(f"emekliliğinize {emeklilik} yıl kaldı")
   else:
      print(f"zaten emekli oldun {isim}")

EmekliligeKacYilKaldi(2003,"onur") 

print(help(EmekliligeKacYilKaldi))




list=[1,2,3]

print(help(list.append))