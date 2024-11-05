numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

val=min(numbers) #numbers listesinin en küçük elemanını yazar
print(val)

val=max(numbers) #numbers listesinin en büyük elemanını yazar
print(val)

val=min(letters) #letters listesinin alfabetik olarak ilk gelen elemanını yazar
print(val)

val=max(letters) #letters listesinin alfabetik olarak son gelen elemanını yazar
print(val)

val=numbers[3:6] #numbers listesinin 3.index elemanından itibaren 6.index elemanına kadar al "16, 4, 9" değerlerini alıcak
print(val)

numbers.append("49") # numbers listesinin sonuna  bir eleman eklemek için kullanılır 

numbers.insert(3,7) # ilk verdiğimiz değer index numarası ikinci verdiğimiz değer ise o index numarasına ekleyiceğimiz değer. bu methodun append den farkı istediğimiz indexe eleman ekleyebiliyoruz
print(numbers)

numbers.pop(2) #listenin istenilen indexteki elemanını siler burada 2.indexteki eleman silinir
print(numbers)

numbers.remove(10) #burada ise index numarası yerine direkt olarak silmek istediğimiz elemanı veriyoruz.

numbers.sort() # liste sayısal büyüklük olarak sıralanır

letters.sort() # liste alfabetik olarak sıralanır

numbers.reverse() # listeyi tersine çevirir

print(len(numbers)) # listenin kaç elemanlı olduğunu söyler

print(numbers.count(10)) # listenin içinde kaç tane 10 değeri var onu söyler

numbers.clear() # bütün elemanları silmek için kullanılır

