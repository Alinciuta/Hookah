# def add(x, y):
#     return x + y
#
#
# print(add(2, 3))
#
# def functia_mea(*args):
#     return args
#
#
# print(functia_mea(1, 2, 3, 4, 5))
#
#
# address = ("Bucuresti", 56, "Cluj", "Ilfov", "Romania")
# street, *rest = address
# print(street)
# print(rest)

# def functie_kwargs(**kwargs):
#     for x, y in kwargs.items():
#         print(x, y)
#     return kwargs
#
# print(functie_kwargs(city = 'Bucuresti',street = 'Pipera'))
# print(type(functie_kwargs(city = 'Bucuresti',street = 'Pipera')))

# def my_func(*args, **kwargs):
#     arguments = {
#         'args': args,
#         'kwargs': kwargs
#     }
#     return arguments
#
# # print(my_func(1,2,3,4,5, city = 'Cluj', street ="Unirii"))
# #
# # print(my_func(city='Cluj'))
# def my_fun(any_number, other_nr, *args, city='Cluj', **kwargs):
#     argument = {
#         'args': args,
#         'kwargs': kwargs
#     }
#     return argument
#
# print(my_fun(1000, 2000, 44, 55, city='Cluj', country = 'Ro'))

# var = None
#
# def mf():
#     global var
#     var = 20
#     return var
#
#
# mf()
# print(var)
#
# var = 30
# print(var)
#
# def sum(x, y):
#     return x +y
#
#
# try:
#     suma = sum(2, 3)
#     print('hello')
# except Exception as e:
#     print('exceptie', e)
# else:
#     print('nimic')
# finally:
#     print('final')
#     # else si finally nu sunt obligatorii la try-except

class ExceptionForNonString(Exception):

    def _init_(self, message):
        self.message = message

    def _str_(self):
        return  self.message

try:
    input1 = input('numele tau: ')
    if type(int(input1)) != str:
        raise ExceptionForNonString
except ExceptionForNonString:
    print('nu e string')
except Exception as e:
    print(e)
