#exc 3

str = input('pls enter your math string : ')

x = range(str.__len__())
list1 = []
num = ''
for i in x:
    if str[i] == ' ' or str[i] == '/' or str[i] == '+' or str[i] == '=' or str[i] == ',' or str[i] == '*' or str[i] == '-' or str[i] == '^':
       if num != '':
          list1.append(num)
          num =''
       list1.append(str[i])
    else:
        num += str[i]
if num != '':
 list1.append(num)
print(list1)
