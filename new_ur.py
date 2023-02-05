from config import token
def calc(price: float, col: int) -> float:
    '''
    :param price:
    :param col:
    :return:
    '''
    return price * col
# print(calc(2.99, 4))
a = 1_000_000_000
# print(a)
# func()
def decor(f):
    def wrapper():
        print('Start')
        f()
        f()
        print('End')
    return wrapper
# s = decor(func)
# s()
# @decor
# @decor
def func():
    print('hello')
# func()

d = (i for i in range(10))
# print(type(d))
# for i in d:
#     print(i)
# print(d)
# print(next(d))
# print(next(d))

# c = list(range(10000000000000))
# c = (i for i in range(10000000000000))
# d = [i for i in range(10000)]
# for i in c:
#     print(i)
# print(next(c))
# print(next(c))
# print(c.__sizeof__(), d.__sizeof__())
# q = (i for i in range(3))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# q = (i for i in range(10))
# print(list(q))
# print(list(q))
# print(list(q))

def func():
    return [1, 2, 3]
# print(func())

def func2():
    for i in [1, 2, 3]:
        yield i

genfunc = func2()
# print(next(genfunc))
# print(next(genfunc))
# print(next(genfunc))
# print(next(genfunc))
'''
for i in func2():
    print(i)
'''
#
'''
def gen_func():
    for i in [1, 2, 3]:
        yield i
        print('Next - >')
for i in gen_func():
    print(i)
'''
#filter
'''
a = [1, 2, 43, 5, 6, 7, 8, 3, 33, 2]
b = list(filter(lambda x: x > 10, a))
print(b)

def square(num):
    return num * num

#map
c = map(square, a)
print(list(c))

#zip
number = [12, 10, 6]
name_user = ['Masha', 'Petya', 'Vasya']
zipvalue = zip(name_user, number)
list_zipvalue = list(zipvalue)
my_dict = dict(list_zipvalue)
print(my_dict)
'''
#
'''
my_list = [1, 2, 4, 5]
print(type(my_list))
my_list = iter(my_list)
print(type(my_list))
print(next(my_list))
print(next(my_list))
'''
s = 'Hello world'
def my_count(s, char):
    index_list = []
    count_word = 0
    count = -1
    for i in s:
        count += 1
        if i == char:
            count_word += 1
            index_list.append(count)
    return count_word, index_list
print(my_count(s, 'l'))