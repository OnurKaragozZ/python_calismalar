# def square(num): return num ** 2

# square=lambda num: num ** 2

numbers=[1,2,3,4,5,6,10,12,15]

# result=list(map(lambda num: num ** 2,numbers)) burada map in yaptığı dizinin elemanlarını fonksiyona tek tek göndermek

# result=list(map(square,numbers)) ilk değere fonksiyon ismini ikinci değere diziyi

# result=square(3)

# print(result)


# for item in map(square,numbers):
#     print(item)


def check_even(num):return num%2==0

# result=list(filter(check_even,numbers))
result=list(filter(lambda num:num%2==0,numbers)) #lamda tek sefer kullanıcağımız fonksiyonlar için kullanılır
print(result)