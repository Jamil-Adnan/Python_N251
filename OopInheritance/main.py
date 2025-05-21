from Mobile import Mobile
from Tv import Tv

SonyTV = Tv("Sony", "Bravia", 56, "4K Ultra HD", 1299, True, 8)
SharpTV = Tv("Sharp", "KT48", 48, "LCD", 999, True, 12)
Apple = Mobile("Apple", "Iphone 16 Pro Max", "IOS", 14, 1400, False, 0)
Samsung = Mobile("Samsung", "Galaxy S24 Ultra", "Android", 200, 600, True, 18)

print (f"{SonyTV} \n")
print (f"{SharpTV} \n")

print (f"{Apple} \n")
print (f"{Samsung}\n")

SonyTV.TurnOn()
SharpTV.TurnOff()
SonyTV.Channel()

Apple.Call()
Samsung.Sms()