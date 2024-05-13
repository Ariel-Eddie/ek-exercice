# Exercice Forward to the Past :

L'équipe de production de "Back to the Future" souhaite refaire la promotion de sa saga avec une stratégie marketing incluant des réductions sur l'achat de leurs DVD.
Nous voulons calculer automatiquement les réductions à appliquer en fonction du panier d'achat.
Ce repo implémente une solution simple qui adresse ce problème.

# Spécifications :

- Prix :
    - Prix des DVDs 'Back to the Future' : 15
    - Prix des autres DVDs : 20

- Réductions :
    - 10 % de réduction sur l'ensemble des DVDs 'Back to the Future' si le panier contient **02** volets différents
    - 20 % de réduction sur l'ensemble des DVDs 'Back to the Future' si le panier contient **03** volets différents

# Comment utiliser :

- Entrée : Chaîne de caractères. Des retours à la ligne sont attendus comme séparation des différents noms de DVD.
- Sortie : Prix (int/float)

Pour utiliser le code sans l'interface Streamlit, il suffit d'importer la fonction `get_final_price` et de lui passer la chaîne de caractères en entrée :
```
from app import get_final_price

basket = """
Back to the Future 1
Back to the Future 2
Back to the Future 3
"""

print(get_final_price(basket))
```

Pour utiliser l'interface Streamlit, il faut installer le package 'streamlit' et exécuter la commande suivante :
```
pip install streamlit
```
ou 
```
pip install -r requirements.txt
```

Ensuite :
```
streamlit run app.py
```
