# Curst 14 octombrie
# lista = [1, 2, 3, 4]
# for index, value in enumerate(lista):
#     print(index, '=>', value)
#
# x = 'mere'
# # x[0] = 'p'
# y = x.replace('m', 'p')
# print(y)
#
# a = 'Ana are mere'
# print(a.split(' '))
# #
# a = ('a', False, 4, ('tuple', 3), 'soare')
#
# list(a)
# print(list(a))
# # b = ('a',)  #Ca un element sa fie Tuplu trebuie sa aiba virgula
# # # print(type(a))
# # # print(type(b))
#
# y = ('b', 4)
# print(a+y)  #Putem concatena stringuri si tupluri
# for i in y:
#     print(i)
# # y[0] = 'a'

#  LISTA
# x = ['a', False, 4, ('tuple', 3), 'soare']
# for i in x:
#     print(i)
#
# x[0] = 'b'
# print(x)
# y = [['123', False, 'abc', 'e'], [1], 'a', True, ['7', 'cdef']]
# print(y[0][2][1]) #Acceseaza B-ul din abc
# print(y[4][1][3])
# print(str(y[0][0][2])) #nr 3 din primul cuv
#
# y.append(2)
# y.insert(2, 'alo')
# print(y)
# print(y[::2]) # Afiseasa elementele din 2 in 2

#  SET
# s = {1, 2,7, 'a', 3, 4, 5}  # Setul are doar elemente unice
# s.add(6)
# print(s)
# for x in set(s):
#     print(x)
# a = [1, 2, 3]
# b = [4, 5, 2]
# print(set(a) | set(b))
# print(set(a) - set(b))
# (s.discard(3))
# print(s)

# DICTIONAR
# a = {1: 'abv',
#      '2': [1, 2, 3],
#      (1, 2): 'a'}
# for x in a.keys():
#     print(x)
# a[2] = 'fff'
# print(a)

taskuri = ['citit', 'scris', 'vorbit']
a = None
while a != '0':
    a = input(' Introdu task: ')
    taskuri.append(a)
    print(taskuri)
