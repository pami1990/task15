# exc 2

def piglatin(str):
    if str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o':
        str1 = str + 'way'
    else:
        x = range(str.__len__())
        str3 = ''
        for i in x:
            if str[0] != 'a' and str[0] != 'e' and str[0] != 'i' and str[0] != 'o':
               str3 += str[0]
               #print(str)
               str = str.replace(str[0], '')
        str1 = str + str3 + 'ay'
    return str1


sentence = input('pls enter your sentence : ')
words = sentence.split(' ')
x = range(words.__len__())
new_sen = ''
for i in x:
    new_sen = (new_sen + ' ' + piglatin(words[i]))

print(new_sen)