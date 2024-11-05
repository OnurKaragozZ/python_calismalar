# 1- "bmw, mercedes ,opel, mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar=["bmw","mercedes","opel","mazda"]

# 2- Liste kaç elemanlıdır?

result=len(arabalar)
print(result)

# 3- listenin ilk ve son elemanı nedir?

print(arabalar[0])
print(arabalar[-1])

# 4- mazda değerini toyota ile değiştirin.

arabalar[-1]="toyota"
result=arabalar

# 5- mercedes listenin bir elemanı mıdır?

result="mercedes" in arabalar

# 6- listenin  -2 indexsindeki değer nedir?

result=arabalar[-2]

# 7- listenin ilk 3 elemanını alın.

result=arabalar[0:3]

# 8- listenin son 2 elemanı yerine "toyota" ve "renaultt" değerlerini ekleyin.

arabalar[-2:]=["toyota","renault"]
result=arabalar

# 9- listenin üzerine "audi" ve "nissan" değerlerini ekleyin.

result=arabalar.append("audi")
result=arabalar.append("nissan")
result=arabalar
print(result)

# 10-listenin son elemanını silin.

del arabalar[-1]

# 11-listenin elemanlarını tersten yazdırınız.

result=arabalar[::-1]

# 12-aşağıdaki verileri bir liste içinde saklayınız.

    # studentA: yiğit bilgi 2010, (70,60,70)
    # studentB: sena turan 1999, (80,80,70)
    # studentC: ahmet turan 1998, (80,70,90)

studentA=["yiğit","bilgi",2010,[70,60,70]]
studentB=["sena","turan",1999,(80,80,70)]
studentC=["ahmet","turan",1998,(80,70,90)]
    
