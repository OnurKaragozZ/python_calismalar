"""

soru: girilen bir sayının asal olup olmadığını bulun.
** asal sayı bir ve kendisi hariç tam böleni olmayan sayılara denir.

"""

sayi=int(input("sayı giriniz: "))
asalmi=True


if sayi==1:
    asalmi=False

for i in range(2,sayi):
    if sayi%i==0:
        asalmi=False
        break
    
if asalmi:
    print("sayı asaldır")
else:
    print("sayı asal değildir")