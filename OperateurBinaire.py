from fct_utile import joinable, AttributesError, isarginrel, Relation, havesameattributes


def join(rel1, rel2):
    """Fonction qui retourne une relation dont le name est la traduction de la jonction en SPJRUD en SQL
    et le attributes est un dictionnaire qui décrit superficiellement la relation obtenue par la jonction
    (mêmes attributs et types de valeurs)

    :param rel1: Une instance de Relation
    :param rel2: Une instance de Relation
    :return: new_rel: Une instance de Relation dont le name est une requête en SQL
    :raise AttributesError
    """

    if joinable(rel1, rel2):
        name = f"(SELECT * FROM {rel1.name} NATURAL JOIN {rel2.name})"
    else:
        raise AttributesError("Jonction impossible car aucun attribut en commun")

    attributes = {}
    for arg in rel1.attributes:
        if type(rel1.attributes[arg][0]) == int:
            attributes[arg] = [1]
        elif type(rel1.attributes[arg][0]) == str:
            attributes[arg] = ["a"]
        else:
            attributes[arg] = []

    for arg in rel2.attributes:
        if not isarginrel(arg, rel1):
            if type(rel2.attributes[arg][0]) == int:
                attributes[arg] = [1]
            elif type(rel2.attributes[arg][0]) == str:
                attributes[arg] = ["a"]
            else:
                attributes[arg] = []

    new_rel = Relation(name, attributes)
    return new_rel


def union(rel1, rel2):
    """Fonction qui retourne une relation dont le name est la traduction de l'union en SPJRUD en SQL
    et le attributes est le attributes d'une des relations en paramètre

    :param rel1: Une instance de Relation
    :param rel2: Une instance de Relation
    :return: new_rel: Une instance de Relation dont le name est une requête en SQL
    :raise AttributesError
    """

    if havesameattributes(rel1, rel2):
        name = f"(SELECT * FROM {rel1.name} UNION SELECT * FROM {rel2.name})"
    else:
        raise AttributesError(f"Union impossible car attributs de {rel1.name} différent de {rel2.name} ")
    new_rel = Relation(name, rel1.attributes)
    return new_rel


def difference(rel1, rel2):
    """Fonction qui retourne une relation dont le name est la traduction de la différence en SPJRUD en SQL
    et le attributes est le attributes d'une des relations en paramètre

    :param rel1: Une instance de Relation
    :param rel2: Une instance de Relation
    :return: new_rel: Une instance de Relation dont le name est une requête en SQL
    :raise AttributesError
    """

    if havesameattributes(rel1, rel2):
        name = f"(SELECT * FROM {rel1.name} EXCEPT SELECT * FROM {rel2.name})"
    else:
        raise AttributesError(f"Différence impossible car attributs de {rel1.name} différent de {rel2.name} ")
    new_rel = Relation(name, rel1.attributes)
    return new_rel
