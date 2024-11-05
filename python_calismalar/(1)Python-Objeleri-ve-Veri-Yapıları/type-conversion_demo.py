"""
Daire Alanı   : pi*r*r
Daire Çevresi : 2*pi*r

    *Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.(pi=3,14)

"""

pi=3.14
r=input("Daire yarıçapını giriniz: ")

alan=pi*int(r)*int(r)
cevre=2*pi*int(r)

print("alan: ",alan)
print("çevre: ",cevre)

