'''Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
'''
def odd_nums(end):
    for i in range(1, end+1, 2):
        yield i

odd_to_15 = odd_nums(15)
next(odd_to_15)