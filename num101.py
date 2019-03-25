import numpy as np 
a=['Andi','Budi','Caca']
b=np.array(a)
# # print(a) #['Andi', 'Budi', 'Caca']
# # print(b) #['Andi' 'Budi' 'Caca']
# # print(a[0]) #Andi
# # print(b[0]) #Andi
# ##print(a[0]+'Susilo') Andi Susilo
# ##print(b[0]+'Susilo') Andi Susilo
c=[1,2,3]
d=np.array([a,c]) #harus array 2 dimensi
# # print(d[0]) #hasilnya a
# # print(d[1]) #hasilnya c
# # print(d[0][1]) #Budi
# # print(d[0,1]) #Budi
print(d.ndim) #dimensi 2, karena ada 2 index; kalau 3, print (contoh[:][:][:])
print(d.size) #jumlah elemen=6
print(d.itemsize) #jumlah masing2 elemen di array dalam byte; int32=4, int64=8, str ada ditengah=84
print(d.dtype) #int32 campur <U11
print(d.shape) #bentuknya gimana berapa baris, kolom
####=============================================================
dua=np.array([[1,2,3],[4,5,6]])
print(dua)
print(dua.shape)
dua=dua.reshape(1,6) #reshape harus tau sizenya, terus 2 faktor dikali adalah size tersebut
print(dua)
print(dua.shape)
'''
##d.shape
#contoh [[1,2,3],[1,2,3]] jawabnya (2,3) berarti 2 list dan 3 element masing2 array
#satu dimensi (jumlah,) 
'''

##ndim
e=np.array([a,b,a])
print(e) #isinya [[a...],[b...],[a...]] tetep 2 dimensi
print(np.array(e).ndim)


##Slicing
tiga=np.array([[1,2,3],[4,5,6],[8,9,1],[10,11,2]])
print(tiga[0:2]) #ambil semua index 0 dan 1
print(tiga[0:3,[0,2]]) #ambil semua list 0-2 yang indexnya 0 dan 2
print(tiga[1::2,1]) #ambil yang list ganjil dan index ke 1


## Akses untuk merubah nilai
tiga[:,1]+=2
print(tiga)
print(tiga.max())
print(tiga.min())
print(tiga.sum())
print(tiga.sum(axis=0)) #kolom; elemen 1=1+4+8+10 elemen2=2+5+9+11 dan seterusnya
print(tiga.sum(axis=1)) #baris; elemen 1=1+2+3 elemen 2=4+5+6 dan seterusnya
# ##print(tiga.sum(axis=2)) #axis cuma tidak sampai 2 karena cuma 2 dimensi
print(np.sqrt(tiga)) #akar 2
# ##list biasa tidak bisa sum, tapi bisa rootsquare
print(np.std(tiga))
# #standar deviasi =(akar dari (n(jumlah xi)**2-xi**2)/n(n-1))

'''
BUAT LIST DARI RANGE TERTENTU/ MENCARI TITIK POIN TERTENTU
'''
coba=np.linspace(1,10,10) #bikin 10 data dari 1-10 # (1,10,19) #bikin 19 dari 1-10=1,1.5,...
print(coba)
keempat=[1,2,3]
kelima=[4,5,6]
print(keempat+kelima)#[1,2,3,4,5,6]
keenam=np.array(keempat)
ketujuh=np.array(kelima)
print(keenam+ketujuh) #seperti sum array 0
# ##print(kelima-keempat) #Error
print(keenam-ketujuh)
print(keenam/ketujuh)
print(ketujuh.ravel()) #gabung jadi satu dimensi kalau [[1,2,3],[4,5,6]]=[1,2,3,4,5,6]
print(np.vstack((keenam,ketujuh)) )#gabung jadi satu list, tapi baris 1 list input1, baris 2 list input2
print(np.hstack((keenam,ketujuh))) #gabung jadi satu horizontal mirip ravel

'''
Buat list dari range tertentu, looping sangat cepat
'''
print(np.arange(1,100,2)) ##(1-99)
print(len(np.arange(1,100,2)))

'''
Trigonometri
'''
print(np.pi)
print(np.rad2deg(np.pi)) ##convert to degree
print(np.cos(45*(np.pi)/180)) ## pi/180
print(np.cos(np.deg2rad(45))) ##trigono ke radian
'''
Logaritma
'''
print(np.log([1,2,3])) #ln e =2.78
print(np.log10([100,10000]))
##log3(x)=log10(x)/log10(3)
'''
eksponensial
'''
print(np.exp([1,2,3]))
'''
repeat
'''
## buat angka 1 sebanyak berapa kali
angka=1
namalist=[1,2,3,4]
np.repeat(angka,len(namalist))

'''
flatnonzero
'''
##cari nilai yang bukan nol
x=np.arange(-2,3)
print(x)
##array([-2,-1,0,1,2])
print(np.flatnonzero(x)) #index
##array([0,1,3,4])
print(x.ravel()[np.flatnonzero(x)]) #cari nilai berdasarkan index
##arraay([-2,-1,1,2])