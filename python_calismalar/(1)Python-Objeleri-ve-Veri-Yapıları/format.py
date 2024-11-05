name="onur"
surname="karagöz"
age=21

print("my name is {} {}".format(name,surname)) #burada onur karagöz 

print("my name is {1} {0}".format(name,surname)) #burada karagöz onur

print("my name is {n} {s}".format(n=name,s=surname)) #burada değişkenlere isim verdik ve süslü parantezlerin içine verdiğimiz isimleri girdi

print("my name is {n} {s}. I am {a} years old.".format(n=name,s=surname,a=age)) 

result=200/700
print("the result is {r:10.4}".format(r=result)) # ilk girdiğimiz 10 parametresi 10 karakterlik bir alan bırakır ikinci girdiğimiz parametre ise float değerler için virgülden sonra kaç karakter olsun onu belirler


print(f"my name is {name} {surname}. I am {age} years old.") 
