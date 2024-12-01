from collections import Counter
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

def similarity_score(list_a, list_b):
    # Compter les occurrences de chaque élément dans la deuxième liste
    count_b = Counter(list_b)  # Ex. {3: 3, 4: 1, 5: 1, 9: 1}
    
    score = 0
    for num in list_a:
        # Multiplier le nombre par ses occurrences dans list_b
        score += num * count_b.get(num, 0)  # Si `num` n'est pas dans `list_b`, retourne 0
    
    return score

# Exemple
# list_a = [3, 4, 2, 1, 3, 3]
# list_b = [4, 3, 5, 3, 9, 3]

# URL de la page et cookie de session
url = "https://adventofcode.com/2024/day/1/input"
session_cookie = ""

# Récupérer les données et les parser
raw_data = fetch_input(url, session_cookie)
list_a, list_b = parse_input(raw_data)

# Trier les listes (optionnel, selon votre code)
list_a.sort()
list_b.sort()

result = similarity_score(list_a, list_b)
print(result)  # Affichera 31
