import math

#fungsi luas persegi panjang
def luaspersegipanjang(p,l):
    return p * l

#fungsi keliling persegi panjang
def kelilingpersegipanjang(p,l):
    return 2*(p+l)

#fungsi luas bujur sangkar
def luasbujursangkar(s):
    return s*s

#fungsi keliling bujur sangkar
def kelilingbujursangkar(s):
    return 4*s

#fungsi luas lingkaran
def luaslingkaran(r):
    return math.pi *r *r

#fungsi keliling lingkaran
def kelilinglingkaran(r):
    return 2* math.pi *r

#fungsi luas segitiga
def luassegitiga(a,t):
    return (a*t)/2
#fungsi keliling segitiga
def kelilingsegitiga(a,b,c):
    return a+b+c