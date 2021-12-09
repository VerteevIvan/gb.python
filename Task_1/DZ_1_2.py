print('Задание №2')

cubes = [x**3 for x in range(1000) if x % 2 != 0]
print(cubes)
cubes_7 = []

for i in range(len(cubes)):
    if cubes[i] > 0:
     cubes[i] = cubes[i] % 10 + (cubes[i] % 10**2) // 10 + (cubes[i] % 10**3) // 10**2 + (cubes[i] % 10**4) // 10**3 + (cubes[i] % 10**5) // 10**4
print(cubes)

for i in range(len(cubes)):
    if cubes[i] % 7 == 0:
        cubes_7.append(cubes[i])
print("Числа в списке кратные 7:", cubes_7)

cubes = [(x**3)+17 for x in range(1000) if x%2 != 0]
print(cubes)
cubes_7 = []

for i in range(len(cubes)):
    if cubes[i] > 0:
     cubes[i] = cubes[i] % 10 + (cubes[i] % 10**2) // 10 + (cubes[i] % 10**3) // 10**2 + (cubes[i] % 10**4) // 10**3 + (cubes[i] % 10**5) // 10**4
print(cubes)

for i in range(len(cubes)):
    if cubes[i] % 7 == 0:
        cubes_7.append(cubes[i])
print("Числа в списке кратные 7:", cubes_7)

