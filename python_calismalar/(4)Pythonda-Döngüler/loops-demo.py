"""

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
** "random modülü"  için "python random" şeklinde arama yapın.
**100 üzerinden puanlama yapın. her soru 20 puan.
**hak bilgisini kullanıcıdan alın 

"""

import random

sayi=random.randint(1,100)
hak=int(input("hak sayısı: "))
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin: "))

    if sayi==tahmin:
        print(f"tebrikler  {sayac} defada bildiniz. toplam puanınız: {100-((20)*(sayac-1))}")
        break
    elif sayi>tahmin:
        print("yukarı")
    else:
        print("aşağı")
    
    if hak==0:
        print(f"hakkınız bitti. tutulan sayı: {sayi} ")