x=6

hak=5
devam="e"

result=5<x<10
print(result)

# and

result=(x>5) and (x <10) #true ,true => true her iki taraf da true gelmesi lazım ki ture olsun
result=(hak>0) and (devam=="e")

# or

result=(x>0) or (x%2==0) # bir tanesi true olduğu zaman  cevap true olur her ikisinin de true olma zorunluluğu yok
#her ikisi de false olursa cevap false olur false , false => false

# not

result=not(x>0) #normalde x>0 dır ve true değer verir ama not kullandığımız için değer false olur 
