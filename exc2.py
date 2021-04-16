#exc 2

def piglatin(str):

      if str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o':
        str = str + 'way'
      else:
        x = range(str.__len__())
        for i in x:
           if str[i] != 'a' or str[i] != 'e' or str[i] != 'i' or str[i] != 'o':
             str.replace(str[i],'')
        str = str + 'ay'

      return str


sentence = input('pls enter your sentence : ')
words = sentence.split(' ')
x = range(words.__len__())
new_sen = ''
for i in x:
    new_sen = piglatin(words[i]) + ' '
print(new_sen)