import os
import glob
import gzip
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#tra ve folder hien hanh
print(os.getcwd())

#noi string
print(os.path.join('/images/', 'img1.png'))

#tach path va filename
pathname = 'D:/check function/quang.txt'
(dir_name, file_name) = os.path.split(pathname)
print(dir_name)
print(file_name)

#############################################################

#get all path of files have '.jpg'
list_of_path = glob.glob('images/*.png')
print(len(list_of_path))

#############################################################

#make file gzip
data = 'quang is a good man'
f = gzip.open('file.txt.gz','wb')
f.write(data.encode())
f.close()
#read file gzip
f = gzip.open('file.txt.gz', 'rb')
file_data = f.read()
print(file_data.decode())
f.close()

#############################################################

# make a numpy array has 1-way( 1 chieu)
a = np.array([1,2,3])

print(type(a))               #in ra class numpy ndarray
print(a.shape)               #in ra "(3, )"
print(a[0], a[1], a[2])      # in ra 1, 2, 3
a[1] = 7                     #thay doi gia tri 1 phan tu trong mang
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

#tao mot numpy aray co 2 chieu
#kieur unsigned int 8 bit(chua gia tri tu 0 den 255)
width = 300
height = 250
image = np.zeros((width, height), np.uint8)
print(image)

##############################################################
#doc file anh
im = Image.open("../Data/Sydney-Opera-House.jpg")

#chuyen sang anh grayscale
img = im.convert('L')

#resize anh
out = im.resize((128,128))

#rotate anh 45 do
out = im.rotate(45)

# hien thi anh goc va anh ket qua
im.show()
out.show()

##################################################################

x_data = [0,1,2,3]
y_data = [1,3,4,2]
plt.plot(x_data,y_data)
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
