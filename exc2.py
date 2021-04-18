# exc 2

def piglatin(str):
    if str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o':
        str1 = str + 'way'
    else:
        x = range(str.__len__())
        for i in x:
            if str[0] != 'a' and str[0] != 'e' and str[0] != 'i' and str[0] != 'o':
               str = str.replace(str[0], '')
               #print(str)
        str1 = str + 'ay'
    return str1


sentence = input('pls enter your sentence : ')
words = sentence.split(' ')
x = range(words.__len__())
new_sen = ''
for i in x:
    new_sen = new_sen + ' ' + piglatin(words[i])

print(new_sen)