"""
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать
и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

import task_4_2
import sys

print(task_4_2.currency_rates(sys.argv[1]))