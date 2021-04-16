#exc 1

my_mat = [[0, 10, 3], [9, 0, 7], [6, 5, 11]]
x = range(3)
row1 = []
col1 = []
col2 = []
col3 = []

for i in x:
    row1 = my_mat[i]
    col1.append(row1[0])
    col2.append(row1[1])
    col3.append(row1[2])
col1.sort()
col2.sort()
col3.sort()
print(col1[-1], col2[-1], col3[-1])
print(col1, col2, col3)