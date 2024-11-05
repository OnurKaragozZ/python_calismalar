SadikHesap={
    "ad":"sadık turan",
    "hesapNo":"123456",
    "bakiye":3000,
    "ekHesap":2000
}

AliHesap={
    "ad":"Ali turan",
    "hesapNo":"12345678",
    "bakiye":2000,
    "ekHesap":1000
}


def paraCek(hesap,miktar):
    print(f"merhaba {hesap["ad"]}")

    if (hesap["bakiye"]>=miktar):
        hesap["bakiye"]-=miktar
        print("paranızı alabilirsiniz")
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]

        if (toplam>=miktar):
            ekHesapKullan=input("ek hesap kullanılsın mı(e/h)")

            if ekHesapKullan=="e":
                ekHesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["ekHesap"]-=ekHesapKullanilacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır")

        else:
            print("üzgünüz bakiye yetersiz")


def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} tl bulunmaktadır.ek hesabınızın limiti ise {hesap["ekHesap"]} tl bulunmaktadır")

paraCek(SadikHesap,3000)
bakiyeSorgula(SadikHesap)

paraCek(SadikHesap,2000)
bakiyeSorgula(SadikHesap)


