"""
Module principal pour lire le CSV et manipuler les listes.
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='utf8') as f:
        l = f.readlines()
    return [[int(x) for x in line.strip().split(';')] for line in l]

def get_list_k(data, k):
    """Retourne la k-ième liste de données."""
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste."""
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste."""
    return l[-1]

def get_max(l):
    """Retourne le maximum de la liste."""
    return max(l)

def get_min(l):
    """Retourne le minimum de la liste."""
    return min(l)

def get_sum(l):
    """Retourne la somme des éléments de la liste."""
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction principale qui orchestre la lecture et les tests.
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
if __name__ == "__main__":
    main()
