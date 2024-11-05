website="https://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-"course" karakter dizisinde kaç karakter bulunmaktadır ?

print(len(course))

# 2-"website" içinden www karakterlerini alın.

print(website[8:11])

# 3-"website" içinden com karakterlerini alın

print(website[23:26])

# 4-"course" içinden ilk 15 ve son 15 karakterlerini alın.

print(course[:15])
print(course[-15:])

# 5-"course" ifadesini tersten yazdırın

print(course[::-1])


name,surname,age,job="onur","karagöz",21,"mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
# "benim adım onur karagöz, yaşım 21 ve mesleğim mühendis "

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job} ")

# 7- "Hello world" ifadesindeki w harfini "W" ile değiştirin.

result="Hello world"
print(result.replace("w","W"))

# 8- "abc" ifadesini yan yana 3 defa yazdırın.

harfler="abc "*3
print(harfler)