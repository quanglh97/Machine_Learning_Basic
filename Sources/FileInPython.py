
#!/usr/bin/python

# -*- coding: utf8 -*-

import os

#kết nối với file
filepath = 'helloworld.txt'
filehandle = open(filepath,'r')

# data = filehandle.read()
# print(type(data))
# print("---------")
# print(data)

#Đóng kết nối với file
filehandle.close()

#ghi file, ghi đè nếu đã tồn tại
filepath = 'my file.txt'
filehandle = open(filepath, 'w',  encoding="utf-8")
text1 = 'write line 1\n'
text2 = 'write line 2\n'
text3 = "Quang đẹp trai nhất vũ trụ\n"
filehandle.write(text1)
filehandle.write(text2)
filehandle.write(text3)
filehandle.close()

#ghi file, ghi tiếp nếu đã tồn tại.
filehandle = open(filepath,'a', encoding='utf-8')
text1 = "ghi tiếp nội dung file my file.txt"
filehandle.write(text1)
filehandle.close()

#kiem tra file co ton tai ko
check = os.path.exists(filepath)
print("file my file.txt co ton tai ko?", check)
check = os.path.exists("dibenem.txt")
print("file dibenem.txt co ton tai ko?", check)

text1 = "01, Lê Hội Quang, 12345\n02, Lê Thị Kiều Trinh, 7862\n03, Nguyễn Hoàng Diệp, 78912\n"
filehandle = open(filepath, 'a', encoding='utf-8')
text2 = ['00', 'joln', '5468']
st = (',').join(text2)

print(st, type(st), text2, type(text2))
filehandle.write((st))
filehandle.write(text1)
filehandle.close()

filehandle = open(filepath,'r', encoding='utf-8')
data = filehandle.read()
print(data)
print(type(data))
infor = data.split(',')
print(infor)
