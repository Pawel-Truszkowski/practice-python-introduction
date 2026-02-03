# Tworzenie słownika użytkownika
user = {
"name": "Anna",
"age": 28,
"city": "Poznan"
}

# Dostęp do wartości za pomocą klucza
print(user["name"]) # Anna
print(user["city"]) # Poznan

# Dodanie nowej pary klucz-wartość
user["email"] = "anna.nowak@example.com"
print(user) # {"name": "Anna", "age": 28, "city": "Poznan", "email": "anna.nowak@example.com"}

# Zmiana wartości dla istniejącego klucza
user["age"] = 29
print(user) # {"name": "Anna", "age": 29, "city": "Poznan", "email": "anna.nowak@example.com"}

# Usunięcie pary klucz-wartość
del user["city"]
print(user) # {"name": "Anna", "age": 29, "email": "anna.nowak@example.com"}