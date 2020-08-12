list_string = ['lemon','banana','pineaple','orange']
list_s = ['xxxxlemonade','xxxbanana','xxxxpineaple','xxxxorange']

#traditional 
for i in list_string:
    print(i)

#list comprehensions
print('list comprehensions')
[print(i) for i in list_string]

#return list comprehensions 
def return_list(list_string):
    return [print(i) for i in list_string]

return_list(list_s)

s = lambda x: print(x) in list_s
s(list_string)