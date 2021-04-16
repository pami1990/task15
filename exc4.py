# exc 4
dictionary = ['erheat', 'cold', 'cold', 'reheat', 'docl']
query = ['cold', 'heater', 'abcd']


def anagram(string):
    x = range(string.__len__())
    list1 = []
    list2 = []
    my_dict = {}
    for i in x:
        list1.append(string[i])
        a = string.count(string[i])
        list2.append(a)
        if a > 1:
            string.replace(string[i], '')
        my_dict[string[i]] = a

    return my_dict  # print(my_dict)


# dic1 = anagram(str1)
# dic2 = anagram(str2)


x = range(query.__len__())
y = range(dictionary.__len__())
dic1 = {}
dic2 = {}
count = 0
list = []
for i in x:
    dic1 = anagram(query[i])
    for j in y:
        dic2 = anagram(dictionary[j])
        if dic1 == dic2:
            count += 1
    list.append(count)
    count = 0

print(list)
