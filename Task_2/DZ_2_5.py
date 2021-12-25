prise = [23.5, 58.88, 36.65, 9.99, 99.99, 10.55, 88.88, 74.90, 21, 69.2]
'''
print(id(prise))
print(prise)
new_prise = []
for i in range(len(prise)):
    num = prise[i]
    rub = '%02d'%(int(num*100//100))
    cop = '%02d'%(int((num*100)%100))
    new_prise.append(rub + " руб " + cop + " коп")
print(id(new_prise))
print(new_prise)

new_prise.sort()

print(id(new_prise))
print(new_prise[::-1])
'''
print([f'{int(pr)} руб {((pr - int(pr)) * 100):02.0f} коп' for pr in sorted(prise)[::-1][:5]])