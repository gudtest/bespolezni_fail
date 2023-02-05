#1
'''
def polin(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(polin('haha'))
'''
#2
'''
def squar(n):
    return n*n
print(squar(2))
'''
#3
'''
def allsum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(allsum(1, 2, 3))
'''
#4
'''
def my_min(*args):
    n_max = 0
    n_min = 0
    for i in args:
        if i > n_max:
            n_max = i
    n_min = n_max
    for i in args:
        if i < n_min:
            n_min = i
    return n_min
print(my_min(2,4,6,3,2))

def my_min2(*args):
    my_list = list(args)
    my_list.sort()
    return my_list[0]
print(my_min2(2,4,4))
'''
#5
'''
def my_index(s, char):
    count = -1
    if char not in s:
        count = 0
        return count
    else:
        for i in s:
            count += 1
            if i == char:
                break
    return count
print(my_index('hello', 'q'))
'''
#6
'''
def my_upper(s):
    up = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    low = 'qwertyuiopasdfghjklzxcvbnm'
    new_s = ''
    for i in s:
        if i in low:
            new_s += up[low.index(i)]
        else:
            new_s += i
    return new_s
print(my_upper('hElLO'))
'''
#
'''
gl = 1000
def glob_local():
    # gl = 10
    global gl
    #nonlocal
    gl += 10
    return gl
print(glob_local())
'''
#
'''
def recur(num):
    print(num)
    if num < 3:
        recur(num + 1)
    print(num)
recur(1)
'''
#
'''
def factor(n):
    if n <= 0:
        return 1
    else:
        return n * factor(n - 1)
print(factor(6))
'''
#
'''
p = lambda x: x*x
print(p(2))
sum = lambda x, y: x+y
print(sum(5, 6))
my_list = [1, 2, 'hello', lambda x: x**10, 34, 23]
print(my_list[3](2))
'''
#
'''
a = 5
b = 8
if a is b:
    print(id(a), id(b))
    print(True)
c = None
if c is None:
    print(True)
'''
#
'''
my_list = [2, 4, 6, 7, 8, 9, 34, 34, 43, 43, 4, 34]
def list_filter(a, filt=None):
    if filt is None:
        return a
    result = []
    for x in a:
        if filt(x):
            result.append(x)
    return result

r = list_filter(my_list)
r = list_filter(my_list, lambda x: x > 10)
print(r)
'''
#
'''
def your_name(name):
    def sey_hi():
        return f"Hello {name}!"
    return sey_hi
Ivan = your_name('Ivan')
print(Ivan())
'''
#
'''
def counter(start = 0):
    def step():
        nonlocal start
        start += 1
        return start
    return step

counter1 = counter()
print(counter1())
print(counter1())
print(counter1())
counter2 = counter(10)
print(counter2())
print(counter2())
print(counter2())
print(counter2())
'''
#
'''
print('$hello$'.strip('$'))


def del_str(del_char = ' '):
    def go_str(stringa):
        return stringa.strip(del_char)
    return go_str

strip_space = del_str()
strip_baks = del_str('$')
strip_all = del_str('!@#%^&*()')
print(strip_space(' hello '))
print(strip_baks('$$$$hello!'))
print(strip_all('!!!hello!!!'))

def func():
    print('Привет я func!')
func()
def f_decor(f):
    def wrapper():
        print('Start!')
        f()
        print('Stop')
    return wrapper
f_decorator = f_decor(func)
f_decorator()
'''
