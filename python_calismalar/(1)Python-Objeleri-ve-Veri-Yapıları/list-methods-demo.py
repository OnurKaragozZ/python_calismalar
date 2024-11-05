names=["ali","yağmur","hakan","deniz"]
years=[1998,2000,1998,1987]

# 1-"cenk" ismini listenin sonuna ekleyiniz
# names.append("cenk")

# 2-"sena" değerini listenin başına ekleyiniz
# names.insert(0,"sena")

# 3-"deniz" ismini listeden siliniz
# names.remove("deniz")

# 4-"deniz" isminin indexi nedir
# index=names.index("deniz")

# 5-"ali" listenin bir elemanı mıdır
# result="ali" in names

# 6-listenin elemanlarını ters çevirin
# names.reverse()

# 7-listenin elemanlarını alfabetik olarak sıralayınız
# names.sort()

# 8-years listesini rakamsal büyüklüğe göre sıralayınız
# years.sort()

# 9-str ="chavrolet,dacia" karakter dizisini listeye çevirin
# str=["chavrolet","dacia"]
# print(str)

#10-years dizisinin en büyük ve en küçük elemanı nedir
# min=min(years)
# max=max(years)

#11-years dizisinde kaç tane 1998 değeri vardır
# result=years.count(1998)

#12-years dizisinin tüm elemanlarını siliniz
# years.clear()

#13-kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız

markalar=[]

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)