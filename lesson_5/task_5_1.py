'''Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield, например:
'''
def odd_nums(end):
    for i in range(1, end+1, 2):
        yield i

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
#print(next(odd_to_15))

"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), 
не используя ключевое слово yield."""

max_val = 3
odd_nums_gen = (n for n in range(1, max_val + 1, 2))
print(next(odd_nums_gen))