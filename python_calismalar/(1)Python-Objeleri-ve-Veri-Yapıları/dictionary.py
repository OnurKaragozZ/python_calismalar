# key - value

# 41 => kocaeli  34 => istanbul 


# dictionary kullanmadan 

# sehirler=["kocaeli","istanbul"]
# plakalar=[41,34]
# print(plakalar[sehirler.index("kocaeli")])


#dictionary kullanarak
# plakalar={"kocaeli":41 , "istanbul":34}
# print(plakalar["kocaeli"])

# plakalar["ankara"]=6
# print(plakalar)


users={
    "sadikturan":{
        "age":36,
        "roles":["user"],
        "email":"sadik@gmail.com",
        "address":"kocaeli",
        "phone":"123456789"
    },
      "çınarturan":{
        "age":2,
        "roles":["user","admin"],
        "email":"çınar@gmail.com",
        "address":"kocaeli",
        "phone":"1234589"
    }
}

print(users["çınarturan"]["roles"][0]) #user
