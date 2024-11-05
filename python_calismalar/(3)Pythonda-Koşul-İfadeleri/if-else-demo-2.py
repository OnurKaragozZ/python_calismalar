# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# sayi=int(input("sayı giriniz: "))

# if sayi>=0 and sayi<100:
#     print(f"sayınız: {sayi} ve 0-100 arasındadır ")
# else:
#     print(f"sayınız: {sayi} ve 0-100 arasında değil.")

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# sayi=int(input("sayı giriniz: "))

# if sayi>0:
#     if sayi%2==0:
#         print(f"sayınız: {sayi} ve pozitif bir çift sayıdır")
#     else:
#         print(f"sayınız: {sayi} sayınız pozitiftir ancak çift değildir")
# elif sayi==0:
#     print(f"sayınız: {sayi} sayınız sıfırdır")
# else:
#     print(f"sayınız: {sayi} negatif bir sayıdır")    

# 3- email ve parola bilgileri ile giriş kontrolü yapınız.

# email="email@onurkaragoz.com"
# password="abc123"

# girilenEmail=input("email: ")
# girilenPassword=input("parola: ")

# if email==girilenEmail:
#     if password==girilenPassword:
#         print("email ve parola bilginiz doğru ")
#         print("giriş yapıldı")
#     else:
#         print("parola bilginiz hatalı") 
#         print("giriş yapılamadı")
# else:
#     print("email bilginiz hatalı")   


# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))

# if a>b and a>c:
#     print("a en büyük sayıdır")
# elif b>a and b>c:
#     print("b en büyük sayıdır")
# elif c>a and c>b:
#     print("c en büyük sayıdır")


# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) ortalama 50 olsa bile final notu en az 50 olması lazım
# b-) finalden 70 aldığında ortalamanın önemi olmasın

vize1=int(input("vize 1: "))
vize2=int(input("vize 2: "))
final=int(input("final: "))

ortalama=((vize1+vize2)*0.6)+(final*0.4)

# a şıkkı
# if ortalama>=50:
#     if final>=50:
#         print("dersten geçti")
#     else:
#         print("başarısız final notu yetersiz")
# else:
#     print("dersten kaldı")


# b şıkkı
# if ortalama>=50:
#     print("başarılı")
# else:
#     if final>=70:
#         print("ortalama yetmese bile final notu yetiyor. BAŞARILI")
#     else:
#         print("başarısız")


# 6- kişinin ad ,kilo,boy bilgilerini alıp kilo indexslerini hesaplayınız.
# formül: (kilo/boy uzunluğunun karesi)
# aşağıdaki tabloya göre kişi hangi tabloya girmektedir.
# 0-18.4 => zayıf
# 18.5-24.9 => normal
# 25.0-29.9 => fazla kilolu
# 30.0-34.9 => şişman(obez)

ad=input("adınız: ")
kilo=float(input("kilonuz: "))
boy=int(input("boyunuz: "))

index=(kilo/(boy**2))

if index>=0 and index<18.5:
    print("zayıf")
elif index>=18.5 and index<25:
    print("normal")
elif index>=25 and index<30:
    print("fazla kilolu")
elif index>=30 and index<35:
    print("obez")        
else:
    print("bilgileriniz yanlış")