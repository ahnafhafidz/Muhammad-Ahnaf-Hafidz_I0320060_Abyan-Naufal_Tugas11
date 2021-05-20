import geometri2D

p = 10
l = 8

luas = geometri2D.luaspersegipanjang(p,l)
keliling = geometri2D.kelilingpersegipanjang(p,l)

print("PERSEGI PANJANG")
print("Panjang\t\t:", p)
print("Lebar\t\t:", l)
print("Luas\t\t:", luas)
print("Keliling\t:", keliling)

#lingkaran
r = 3

luasling = geometri2D.luaslingkaran(r)
kellingk = geometri2D.kelilinglingkaran(r)

print("LINGKARAN")
print("Jari-jari\t:", r)
print("Luas\t\t:", luasling)
print("Keliling\t:", kellingk)

