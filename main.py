""" ASCII Art - Encodage """
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    chars = [s[0]]
    counts = [1]

    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            counts[-1] += 1
        else:
            chars.append(s[k])
            counts.append(1)

    return list(zip(chars, counts))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    first_char = s[0]
    count = 1
    i = 1
    while i < len(s) and s[i] == first_char:
        count += 1
        i += 1

    return [(first_char, count)] + artcode_r(s[i:])



#### Fonction principale
def main():
    """fonction principale de test des fonctions itérative et récursive"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
