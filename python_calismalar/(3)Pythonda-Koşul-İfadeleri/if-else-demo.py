# 1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

isim=input("isminiz: ")
yas=int(input("yaşınız: "))
egitim=input("eğitim: ")

if yas>=18:
    if egitim=="lise" or egitim=="üniversite":
        print(f"{isim} ehliyet alabilirsin")
    else:
        print(f"{isim} ehliyet alamazsın eğitim durumunuz yetersiz.")
else:
    print(f"{isim} ehliyet alamazsınız yaşınız yetmiyor")


# 2- bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.

# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

yazili1=float(input("yazılı 1: "))
yazili2=float(input("yazılı 2: "))
sozlu=float(input("sözlü : "))

ortalama=(yazili1+yazili2+sozlu)/3

if ortalama>=0 and ortalama<25:
    print(f"ortalamanız: {ortalama} not bilginiz 0")
elif ortalama>=25 and ortalama<45:
    print(f"ortalamanız: {ortalama} not bilginiz 1")
elif ortalama>=45 and ortalama<55:
    print(f"ortalamanız: {ortalama} not bilginiz 2")
elif ortalama>=55 and ortalama<70:
    print(f"ortalamanız: {ortalama} not bilginiz 3")
elif ortalama>=70 and ortalama<85:
    print(f"ortalamanız: {ortalama} not bilginiz 4")  
elif ortalama>=85 and ortalama<=100:
    print(f"ortalamanız: {ortalama} not bilginiz 5")
else:
    print("not ve ortalama bilgisi bulunamadı")         



