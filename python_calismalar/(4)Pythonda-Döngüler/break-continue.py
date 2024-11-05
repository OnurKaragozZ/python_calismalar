# name="onur karagöz"

# for letter in name:
#     if letter=="a":
#         continue
#     print(letter)

#break yaptığımızda direkt döngüden çıkış yaparken continue yaptığımızda sadece o anki döngü turunu iptal ederek tekrar kaldığı yerden devam ediyor
# yukarıdaki kodun çıktısı "onur krgöz" olur çünkü a harfine geldiğinde o anki turu iptal edip kaldığı yerden devam ediyor
#yukarıda break olsaydı ilk a gördüğü yerde dögüden çıkacaktı yani kodun çıktısı "onur k" olucaktı

# x=0

# while x<5:
#     x+=1
#     if x==2:
#         break
#     print(x)

#buradaki kodda x değeri 2 olduğu anda döngüden çıkar ve kodun çıktısı "1" olur
#eğer continue olsaydı kodun çıktısı "1 3 4 5"


#1 -100 e kadar tek sayıların toplamı

x=0
result=0

while x<=100:
    x+=1
    if x%2==0:
        continue
    result+=x

print(f"toplam: {result}")


