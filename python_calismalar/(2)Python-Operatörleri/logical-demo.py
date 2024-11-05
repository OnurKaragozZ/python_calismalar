# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol edin

# sayi=float(input("sayı: "))
# result=(sayi>0) and (sayi<=100)
# print(f"sayi 0-100 arasındamı: {result}")

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin

# sayi=int(input("sayı: "))
# result=(sayi>0) and (sayi%2==0)
# print(f"girilen sayı pozitif çift sayı mı : {result}")

# 3- email ve parola bilgileri ile giriş kontrolü yapın 

# email="email@onurkaragoz.com"
# password="abc123"
# girilenEmail=input("email: ")
# girilenPassword=input("password: ")

# result=(girilenEmail==email) and (girilenPassword==password)
# print(f"uygulamaya giriş başarılımı: {result}")

# 4- girilen  3 sayıyı büyüklük olarak karşılaştırın 

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))

# result= (a>b) and (a>c)
# print(f"a en büyük sayıdır : {result}")

# result= (b>a) and (b>c)
# print(f"b en büyük sayıdır : {result}")

# result= (c>a) and (c>b)
# print(f"c en büyük sayıdır : {result}")

# 5- kullanıcıdan 2 vize (%60) ve final (%40) notu alıp ortalama hesaplayınız 
#    eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a-) ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) finalden 70 aldığında ortalamanın önemi olmasın 


# vize1=float(input("vize 1: "))
# vize2=float(input("vize 2: "))
# final=float(input("final : "))

# ortalama=((vize1+vize2)/2)*0.6 + (final*0.4)
# result=(ortalama>=50) and (final>=50)
# result=(ortalama>=50) or (final>=70)

# print(f"öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}")


# 6- kişinin ad ,kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
# formül:(kilo / boy uzunluğunun karesi)
# aşağıdaki tabloya göre kişi hangi gruba girmektedir
# 0-18.4 => zayıf
# 18.5 - 24.9 => normal
# 25.0 - 29.9 => fazla kilolu
# 30.0 - 34.9 => şişman(obez)


name=input("adınız: ")
kg=float(input("kilonuz: "))
hg=int(input("boyunuz: "))

index=(kg)/(hg**2)
zayif=(index>=0) and (index<=18.4)
normal=(index>18.4) and (index<=24.9)
kilolu=(index>24.9) and (index<=29.9)
obez=(index>29.9) and (index<=34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")
