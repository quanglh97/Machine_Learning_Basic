#ket noi vs file
from os.path import abspath
import os
filename = abspath('../Data//Iris.csv') #chuyen duong dan tuong doi ve tuyet doi
print(filename)
filehandle = open(filename, 'r',  encoding="utf-8")

# readline, doc file theo tung dong
lines = filehandle.readlines()

data = []

min_sepal_length = 1000
min_sepal_wigth = 1000
min_pedal_length = 1000
min_pedal_wigth = 1000

max_sepal_length = 0
max_sepal_wigth = 0
max_pedal_length = 0
max_pedal_wigth = 0

mean_sepal_length = 0
mean_sepal_wigth = 0
mean_pedal_length = 0
mean_pedal_wigth = 0

sum_sepal_length = 0
sum_sepal_wigth = 0
sum_pedal_length = 0
sum_pedal_wigth = 0

num_Iris_setosa = 0
num_Iris_versicolor = 0
num_Iris_virginica  = 0

for i in range(1,len(lines)):
    linesData    = lines[i].split(',')
    sepal_length = float(linesData[1].strip())
    sepal_width  = float(linesData[2].strip())
    pedal_lenght = float(linesData[3].strip())
    pedal_width  = float(linesData[4].strip())



    species = 0
    if linesData[5].strip() == 'Iris-setosa':
        species = 0
    elif linesData[5].strip() == 'Iris-versicolor':
        species = 1
    elif linesData[5].strip() == 'Iris-virginica':
        species = 2

    #print('%s; %s; %s; %s; %s' % (sepal_length, sepal_width, pedal_lenght, pedal_width,species))
    data.append([sepal_length, sepal_width, pedal_lenght, pedal_width, species])

filehandle.close()

for i in range(len(data)):
    if min_sepal_length >= data[i][0]:
        min_sepal_length = data[i][0]
    if min_sepal_wigth >= data[i][1]:
        min_sepal_wigth = data[i][1]

    if min_pedal_length >= data[i][2]:
        min_pedal_length =data[i][2]
    if min_sepal_wigth >= data[i][3]:
        min_pedal_wigth = data[i][3]

    if max_sepal_length <= data[i][0]:
        max_sepal_length = data[i][0]
    if max_sepal_wigth <= data[i][1]:
        max_sepal_wigth = data[i][1]

    if max_pedal_length <= data[i][2]:
        max_pedal_length = data[i][2]
    if max_pedal_wigth <= data[i][3]:
        max_pedal_wigth = data[i][3]

    sum_sepal_length = sum_sepal_length + data[i][0]
    sum_sepal_wigth = sum_sepal_wigth + data[i][1]
    sum_pedal_length = sum_pedal_length + data[i][2]
    sum_pedal_wigth = sum_sepal_wigth + data[i][3]

    if data[i][4] == 0 :
        num_Iris_setosa = num_Iris_setosa + 1
    elif data[i][4] == 1:
        num_Iris_versicolor = num_Iris_versicolor +1
    else:
        num_Iris_virginica = num_Iris_virginica + 1

mean_sepal_length = sum_sepal_length/len(data)
mean_sepal_wigth = sum_sepal_wigth/len(data)
mean_pedal_length = sum_pedal_length/len(data)
mean_pedal_wigth = sum_pedal_wigth/len(data)


print('min_sepal_length = %s\n' %(min_sepal_length))
print('min_sepal_wigth = %s\n' %(min_sepal_wigth))
print('min_pedal_length = %s\n' %(min_pedal_length))
print('min_pedal_wigth = %s\n' %(min_pedal_wigth))

print('max_sepal_length = %s\n' %(max_sepal_length))
print('max_sepal_wigth = %s\n' %(max_sepal_wigth))
print('max_pedal_length = %s\n' %(max_pedal_length))
print('max_pedal_wigth = %s\n' %(max_pedal_wigth))

print('mean_sepal_length = %s\n' %(mean_sepal_length))
print('mean_sepal_wigth = %s\n' %(mean_sepal_wigth))
print('mean_pedal_length = %s\n' %(mean_pedal_length))
print('mean_pedal_wigth = %s\n' %(mean_pedal_wigth))

print('num_Iris_setosa= %s, num_Iris_versicolor = %s, num_Iris_virginica = %s' %(num_Iris_setosa, num_Iris_versicolor, num_Iris_virginica))

#print(len(data))
