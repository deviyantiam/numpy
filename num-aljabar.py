##Matriks
##ALJABAR
##KAGGLE CSV

import numpy as np
# a=np.array([[1,2],[4,5]])
# b=[1,2,3,4,5]
# print(a+a) #penjumlah
# print(b+b) #gabung 2 list
# #print(a+b) #penjumlahan, jika a dan b sama dimensinya
# print(a*a) #dikali sendiri2 #cross product
# print(a@a) #dot product
# print(a.dot(a)) #dot product
# print(a.transpose())
# print(np.linalg.det(a)) #jika perlu di round, determinan
# print(np.linalg.inv(a)) #invers
'''
pembagian matriks
pakai determinan dan invers, terus dikalinya c11=a11*b11+a12*b21
'''
# Pembagian
# a=np.array([[3,-2],[4,-3]])
# b=np.array([[1,-5],[0.5,-3]])
# c=np.linalg.lstsq(a,b,rcond=None)[0]
# print(c)

'''
matriks determinan nol =singular, tidak ada invers
'''
# print(np.mean(a))
# print(np.median(a,axis=0))

##aljabar
# import numpy as np
# a=np.array([[2]]) #2x=3 #2 dimensi variabelnya
# b=np.array([3])
# hasil=np.linalg.solve(a,b) #2 dimensi variablenya
# print(hasil)

'''
4x-3y=1
2x-y=-3
'''
# a=np.array([[4,-3],[2,-1]]) 
# b=np.array([1,-3])
# hasil=np.linalg.solve(a,b)
# print('x=',hasil[0],'y=',hasil[1])

'''
7x+2y=19
4x-3y=15
cari 3x-2y
'''
# a=np.array([[7,2],[4,-3]])
# b=np.array([19,15])
# hasil=np.linalg.solve(a,b)
# akhir=3*hasil[0]-2*hasil[1]
# print(akhir)

'''
3x+5y=17000 dan 4x+2y=18000
cari 20x+30y
'''
# a=np.array([[3,5],[4,2]])
# b=np.array([17000,18000])
# hasil=np.linalg.solve(a,b)
# akhir=20*hasil[0]+30*hasil[1]
# print(akhir)

'''
baca file csv
'''
# # import numpy as np
# # import csv
# # with open('datakaggle.csv','r') as dat:
# #     reader=csv.reader(dat)
# #     for row in reader:
# #         print(row)



# '''
# buat csv dari list
# '''
# import csv
# listku=[
#     ['id','usia'],
#     [1,11],
#     [2,12],
#     [3,13],
#     [4,14],
#     [5,15],
#     [6,16],
#     [7,17],
#     [8,18],
#     [9,19],
#     [10,20]
# ]
# with open('0.csv','w') as fileku: #kalau ada enter maka ('gudang.csv','w',newline='')
#     tulis=csv.writer(fileku,)
#     tulis.writerows(listku)
# import numpy as np
# x=np.loadtxt('0.csv',delimiter=',',skiprows=1)
# y=np.loadtxt('0.csv',delimiter=',',unpack=True,skiprows=1)
# print(x)
# print(y)

# ###atau untuk misahkan baris
# a,b=np.loadtxt('0.csv',delimiter=',',unpack=True,skiprows=1)
# # ##unpack= membuat baris jadi kolom
# print(a)
# print(b)