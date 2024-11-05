numbers=[1,2,3,4,5]

for num in numbers:
    print(num)




names=["onur","çınar","sena"]

for name in names:
    print(f"my name is {name}")




name ="onur karagöz"

for n in name:
    print(n)



tuple=(1,2,3,4,5)

for t in tuple:
    print(t)




tuple=[(1,2),(3,4),(5,8)]

for a,b in tuple:
    print(a)  #burada 1,3,5 yazdırılacak





d={"k1":1,"k2":2,"k3":3}

for item in d:
    print(item) #burada sadece key bilgileri gelicek  "k1" gibi

for item in d.items():
    print(item) #burada eleman grupları gelicek ("k1": 1) gibi

for key,value in d.items():
    print(key) #burada sadece key ler gelir. value dersek de value lar gelir