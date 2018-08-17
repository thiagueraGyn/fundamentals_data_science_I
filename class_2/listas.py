month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use a indexação de lista para definir a variável num_days com quantos dias existem em um mês específico
num_days = days_in_month[7]
print(num_days)


a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

# Tuplas
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

# Conjuntos
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a) # remove valores repetidos
b.add(5) # adiciona um valor
b.pop() # remove um valor aleatorio

# Dicionarios
population = {'Shanghai':17.8, 'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}
print(population)

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

# Compreensão de listas
cities = {}
capitalized_cities = [city.title() for city in cities]

squares = [x**2 for x in range(9) if x % 2 == 0]

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]