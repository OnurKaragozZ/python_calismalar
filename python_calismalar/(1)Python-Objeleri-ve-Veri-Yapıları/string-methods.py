message="Hello There. My name is Onur Karagöz"

message=message.upper() #message içindeki bütün karakterleri büyük harfe çevirir
message=message.lower() #message içindeki bütün karakterleri küçük harfe çevirir
message=message.title() #message içindeki her kelimenin baş harfini büyük harfe çevirir
message=message.capitalize() #message içindeki ilk kelimenin baş harfini büyük harfe çevirir

message=message.strip() #baştaki ve sondaki boşluk karakterlerini silmek için kullanılır
message=message.split(".") #her bir "." dan ayırarak bir liste oluşturur
message=message.split(" ") #her bir " " dan ayırarak bir liste oluşturur

message=" ".join(message) # parça parça olan kelimeleri aralarına boşluk koyarak birleştirir

index=message.find("Onur") #message ın içinde "onur" kelimesi var mı diye arar varsa index numarasını verir eğer o kelime yoksa -1 değerini verir
print(index)

isFound=message.startswith("H") #message "H" ile mi başlıyor bunu kontrol edip bize bool değer döndürür
isFound=message.endswith("z") #message "z" ile mi bitiyor bunu kontrol edip bize bool değer döndürür

message=message.replace(" ","*") #message içinde replace methodunun içine verdiğimiz ilk parametre yerine ikinci parametreyi koyar
message=message.replace(" ","*").replace("ç","c").replace("ö","o") #arka arkaya replace eklenebilir


message=message.center(100,"*")#mesagge yi 100 karakterlik bir alanın ortasına yerleştirir 50 karakterden kalan boşluklara da verdiğimiz ikinci parametreyi ekler 
 
