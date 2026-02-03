# Tworzenie listy
animals = ["dog", "cat", "fish"]

# Dodawanie nowych elementów
animals.append("canary")
animals.append("turtle")

# Usuwanie elementów
animals.remove("fish")

# Aktualizacja elementu
animals[0] = "shepherd"

print(animals) # ['shepherd', 'cat', 'canary', 'turtle']

# Tworzenie listy owoców
fruits = ["apple", "banana", "pear", "grapes", "peach"]

# Wyciąganie fragmentu listy(od indeksu 1 do 3, bez 4)
print(fruits[1:4]) # ['banana', 'pear', 'grapes']

# Wyciąganie co drugiego elementu
print(fruits[::2]) # ['apple', 'pear', 'peach']

# Odwrócenie kolejności elementów
print(fruits[::-1]) # ['peach', 'grapes', 'pear', 'banana', 'apple']
