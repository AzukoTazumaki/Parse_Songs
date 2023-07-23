# f = [1, 2, 3, 4, 5]
# s = ['а', 'б', 'в', 'г', 'д']
# print(zip(f, s))
from random import randint
from datetime import date

result = ''
for i in range(17):
    if i == 0:
        continue
    result += f'("А{randint(100, 300)}"), '
print(result)
