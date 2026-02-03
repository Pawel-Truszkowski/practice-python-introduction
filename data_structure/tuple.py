# Tworzenie krotki
coordinates = (52.2297, 21.0122)

# Dostęp do elementów krotki
print(f"Szer. geograficzna: {coordinates[0]}")
print(f"Dług. geograficzna: {coordinates[1]}")

# Próba zmiany elementu spowoduje błąd
coordinates[0] = 53.0000 # TypeError: 'tuple' object does not