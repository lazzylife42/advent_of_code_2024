import requests

def fetch_input(url, session_cookie):
    # Envoyer la requête HTTP avec le cookie de session
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)

    # Vérifier que la requête a réussi
    if response.status_code != 200:
        raise ValueError(f"Échec de la requête : {response.status_code}")

    return response.text

def parse_input(data):
    list_a = []
    list_b = []
    
    # Parcourir chaque ligne et extraire les deux valeurs
    for line in data.strip().split("\n"):
        a, b = map(int, line.split())  # Convertir les valeurs en entiers
        list_a.append(a)
        list_b.append(b)
    
    return list_a, list_b

def sum_diff(list_a, list_b) -> int:
    if len(list_a) != len(list_b):
        raise ValueError("Les listes doivent être de la même taille.")
    total = 0

    for a, b in zip(list_a, list_b):
        total += abs(a - b)
    
    return total

# URL de la page et cookie de session
url = "https://adventofcode.com/2024/day/1/input"
session_cookie = ""

# Récupérer les données et les parser
raw_data = fetch_input(url, session_cookie)
list_a, list_b = parse_input(raw_data)

# Trier les listes (optionnel, selon votre code)
list_a.sort()
list_b.sort()

# Calculer la somme des différences absolues
result = sum_diff(list_a, list_b)
print(result)
