# 1-100 e kadar 

x=0

while x<=100:
    if x%2==0:
        print(f"sayı çift {x}")
    else:
        print(f"sayı tek: {x}")
    x+=1

print("bitti...")




name="" #false

while not name.strip(): #not name true olur yani bir isim yazana kadar sorucak
    name=input("isminizi girin: ")

print(f"merhaba {name}")


