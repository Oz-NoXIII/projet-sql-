import fct_utile


def join(rel1, rel2):
    """Fonction qui retourne le str qui est la traduction de la jonction en SPJRUD en SQL"""

    if fct_utile.joinable(rel1, rel2):
        sol = f"select * from {rel1.nom} natural join {rel2.nom}"
    else:
        raise fct_utile.ErrorKey("Jonction impossible car aucun attribut en commun")
    return sol


def union():
    pass  # TODO


def difference(rel1, rel2):
    """Fonction qui retourne le str qui est la traduction de la différence en SPJRUD en SQL"""

    if fct_utile.havesameargs(rel1, rel2):
        sol = f"select * from {rel1.nom} except select * from {rel2.nom}"
    else:
        raise fct_utile.ErrorKey(f"Différence impossible car attributs de {rel1.nom} différent de {rel2.nom} ")
    return sol
