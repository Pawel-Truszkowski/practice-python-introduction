# Tworzenie zbioru owoców
fruits = {"apple", "banana", "pear", "apple"}

# Wyświetlenie zbioru (duplikaty są automatycznie usuwane)
print(fruits) # {"apple", "banana", "pear"}

# Dodanie nowego elementu
fruits.add("plum")
print(fruits) # {"apple", "banana", "pear", "plum"}

# Usunięcie elementu
fruits.remove("banana")
print(fruits) # {"apple", "pear", "plum"}

# Tworzenie dwóch zbiorów
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Suma zbiorów (elementy z obu zbiorów)
print(set_a | set_b) # {1, 2, 3, 4, 5, 6}

# Część wspólna zbiorów (elementy wspólne)
print(set_a & set_b) # {3, 4}

# Różnica zbiorów
print(set_a - set_b) # {1, 2}

# Elementy unikalne w obu zbiorach
print(set_a ^ set_b) # {1, 2, 5, 6}