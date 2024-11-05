x,y,z=2,5,10

numbers=1,5,7,10,6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

# sayi1=int(input("sayı 1: "))
# sayi2=int(input("sayı 2: "))

# carpim=sayi1*sayi2
# toplam=x+y+z
# fark=carpim-toplam
# print(fark)

# 2- y'nin x'e kalansız bölümünü hesaplayın

# result=y//x

# 3- (x,y,z) toplamının mod 3'ü nedir?

# toplam=x+y+z
# result=toplam%3
# print(result)

# 4- y'nin x. kuvvetini hesaplayın

# result=y**x
# print(result)

# 5- x,*y,z=numbers işlemine göre z'nin küpü kaçtır

# x,*y,z=numbers  #burada x=1 y=[5,7,10] z=6 cevap 6*6*6=216
# result=z**3
# print(result) 

# 6- x,*y,z=numbers işlemine göre y nin değerleri toplamı kaçtır

x,*y,z=numbers  
result=y[0]+y[1]+y[2]

print(result) 


