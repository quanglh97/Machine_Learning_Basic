from sklearn import tree
#buoc 1: thu thap du lieu
#buoc 2: xu li du lieu
#buoc 3: xay dung model
#buoc 4: du doan ket qua
#buoc 5: danh gia ket qua
my_tree = tree.DecisionTreeClassifier()
dactrung = [[1, 3, 3, 7],
            [5, 2, 4, 6],
            [1, 2, 4, 6],
            [5, 4, 4, 3],
            [1, 4, 4, 7],
            [3, 3, 3, 6],
            [5, 2, 2, 7]]

nhan = [0, 1, 1, 0 , 0, 0, 0]

result = my_tree.fit(dactrung, nhan)

kq = result.predict([[1, 4, 3, 6]])
print(kq)
