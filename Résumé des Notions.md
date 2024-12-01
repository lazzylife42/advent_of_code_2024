
# **Résumé des Fonctions et Concepts en Python**

## **1. Fonctions**
### Définir une fonction
- Une fonction est définie avec le mot-clé `def`, suivi de son nom et de ses paramètres.
- Exemple :
  ```python
  def ma_fonction(param1, param2):
      # Corps de la fonction
      return resultat
  ```

### Points importants :
- Les fonctions peuvent prendre des **paramètres** et retourner une valeur avec `return`.
- En Python, les types des paramètres ne sont pas stricts, mais on peut annoter avec `->` pour donner des indications :
  ```python
  def sum_diff(list_a: list, list_b: list) -> int:
      pass
  ```

---

## **2. Bibliothèque `requests`**
### Qu'est-ce que `requests` ?
- C’est une bibliothèque utilisée pour envoyer des requêtes HTTP, comme GET et POST.
- Elle simplifie l’interaction avec les serveurs web (équivalent de `curl` ou des sockets).

### Exemple :
```python
import requests

response = requests.get("https://example.com")
print(response.text)  # Affiche le contenu de la page
```

### Points clés :
- **Headers** : On peut ajouter des en-têtes comme un cookie pour les requêtes HTTP.
  ```python
  headers = {"Cookie": "session=12345"}
  response = requests.get(url, headers=headers)
  ```

---

## **3. Manipulation de chaînes de caractères**
### Diviser du texte
- **`split()`** : Découpe une chaîne de caractères en liste.
  ```python
  texte = "3 4\n5 6"
  lignes = texte.split("\n")  # ["3 4", "5 6"]
  ```

### Supprimer les espaces inutiles
- **`strip()`** : Enlève les espaces ou caractères inutiles au début et à la fin.
  ```python
  ligne = "  3 4  "
  nettoyee = ligne.strip()  # "3 4"
  ```

### Combiner les méthodes
- **`split("\n")` et `strip()`** : Pour traiter du texte brut ligne par ligne.
  ```python
  for line in data.strip().split("\n"):
      print(line)  # Traite chaque ligne proprement
  ```

---

## **4. Itérateurs et Boucles**
### `for` avec `zip`
- **`zip`** : Combine plusieurs listes ou itérables en une seule séquence d’éléments groupés.
  ```python
  list_a = [1, 2, 3]
  list_b = [4, 5, 6]
  for a, b in zip(list_a, list_b):
      print(a, b)  # Affiche (1, 4), (2, 5), (3, 6)
  ```

### Compter des occurrences avec `collections.Counter`
- **`Counter`** : Une structure de données pour compter les éléments d’une liste.
  ```python
  from collections import Counter

  liste = [3, 3, 4, 5, 3]
  count = Counter(liste)  # {3: 3, 4: 1, 5: 1}
  print(count[3])  # Affiche 3
  ```

### Boucle sur des dictionnaires
- Parcourir un dictionnaire clé-valeur :
  ```python
  count = {"a": 1, "b": 2}
  for key, value in count.items():
      print(f"{key} apparaît {value} fois")
  ```

---

## **5. Gestion des Erreurs**
### Lever une exception
- **`raise`** : Permet d’interrompre le programme avec un message d’erreur clair.
  ```python
  if not condition:
      raise ValueError("Un message d'erreur")
  ```

---

## **6. Fonctions utiles**
### Trier une liste
- **`sort()`** : Trie une liste en place (modifie directement la liste).
  ```python
  liste = [3, 1, 4]
  liste.sort()  # [1, 3, 4]
  ```

### Valeur par défaut avec `dict.get`
- **`get()`** : Récupère une valeur d’un dictionnaire ou retourne une valeur par défaut si la clé n’existe pas.
  ```python
  d = {"a": 1}
  print(d.get("a", 0))  # 1
  print(d.get("b", 0))  # 0
  ```

---

## **7. Mathématiques**
### Calcul de la valeur absolue
- **`abs(x)`** : Renvoie la valeur absolue d’un nombre.
  ```python
  print(abs(-3))  # 3
  ```

---

## **Exemple complet d’utilisation**
Voici un exemple intégrant tout ce que nous avons vu :

```python
from collections import Counter
import requests

def fetch_input(url, session_cookie):
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError("Échec de la requête")
    return response.text

def parse_input(data):
    list_a = []
    list_b = []
    for line in data.strip().split("\n"):
        a, b = map(int, line.split())
        list_a.append(a)
        list_b.append(b)
    return list_a, list_b

def similarity_score(list_a, list_b):
    count_b = Counter(list_b)
    return sum(num * count_b.get(num, 0) for num in list_a)

url = "https://example.com"
session_cookie = "12345"

data = fetch_input(url, session_cookie)
list_a, list_b = parse_input(data)
score = similarity_score(list_a, list_b)
print(score)
```