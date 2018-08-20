from dictionary import Dictionary

# Tworzymy mapowanie nazwy stanu na skrót
states = Dictionary()
states.set('Oregon', 'OR')
states.set('Floryda', 'FL')
states.set('Kalifornia', 'CA')
states.set('Nowy Jork', 'NY')
states.set('Michigan', 'MI')

# Tworzymy podstawowy zestaw stanów i znajdujących się w nich miast
cities = Dictionary()
cities.set('CA', 'San Francisco')
cities.set('MI', 'Detroit')
cities.set('FL', 'Jacksonville')

# Dodajemy kilka miast
cities.set('NY', 'Nowy Jork')
cities.set('OR', 'Portland')

# Drukujemy kilka miast
print('-' * 10)
print("Stan NY ma: %s" % cities.get('NY'))
print("Stn OR ma: %s" % cities.get('OR'))

# Drukujemy kilka stanów
print('-' * 10)
print("Skrót dla Michigan to: %s" % states.get('Michigan'))
print("Skrót dla Florydy to: %s" % states.get('Floryda'))

# Używamy najpierw słownika states, a potem cities
print('-' * 10)
print("Michigan ma: %s" % cities.get(states.get('Michigan')))
print("Floryda ma: %s" % cities.get(states.get('Floryda')))

# Drukujemy skrót każdego stanu
print('-' * 10)
states.list()

# Drukujemy każde miasto w stanie
print('-' * 10)
cities.list()

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Przepraszamy, nie ma stanu Texas.")

# Domyślne wartości przy użyciu ||= z pustym obiektem jako wynikiem
# Możesz zrobić to w jednej linii?
city = cities.get('TX', 'Nie istnieje')
print("Miasto dla stanu 'TX' to: %s" % city)
