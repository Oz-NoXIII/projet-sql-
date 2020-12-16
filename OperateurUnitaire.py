from SQlLiteManage import execute
from fct_utile import removeduplicate, argsinrel, Relation, isarelation, ComparatorError, ErrorType, isarginrel, \
    havesametype, AttributesError


def select(relation, cmp, attrib, const, counter):
    """Fonction qui retourne une relation dont le name est la traduction de la selection en SPJRUD en SQL
    et le attributes est le attributes de la relation en paramètre
    """

    comparators = ['=', '<', '>', '<=', '>=', '!=']
    isarelation(relation.attributes)
    if comparators.count(cmp) == 0:
        raise ComparatorError("L'élément " + cmp + " est invalide pour cette operation. " +
                              f"Veuillez utiliser un des comparateurs suivants:{comparators}")
    if not isarginrel(attrib, relation):
        raise AttributesError(f"{attrib} n'est pas un attribut de la relation {relation.attributes}")

    # counter !=1 => attribut égal constante
    # counter=1 => attribut égal attribut
    if counter == 1:
        if not isarginrel(const, relation):
            raise AttributesError(f"{const} n'est pas un attribut de la relation {relation}")
        args = [relation.attributes[attrib][0], relation.attributes[const][0]]
        havesametype(args)

    else:
        if type(relation.attributes[attrib][0]) != type(const):
            raise ErrorType(
                f"Dans les attributs: {relation.attributes[attrib][0]} et {const} doivent etre du meme type")
    name = f"SELECT * FROM {relation.name} WHERE {attrib}{cmp}{const}"
    new_rel = Relation(name, relation.attributes)
    # execute(new_rel.name)
    return new_rel


def project(relation, *args):
    """Fonction qui retourne une relation dont le name est la traduction de la projection en SPJRUD en SQL
    et le attributes est un dictionnaire qui décrit superficiellement la relation obtenue par la projection
    (mêmes attributs et types de valeurs)"""

    args = removeduplicate(args)
    argsinrel(relation, args)
    name = "SELECT "
    for i in range(len(args)):
        if i != len(args) - 1:
            name += args[i] + ", "
        else:
            name += args[i] + f" FROM {relation.name}"
    attributes = {}
    for arg in args:
        if type(relation.attributes[arg][0]) == int:
            attributes[arg] = [1]
        elif type(relation.attributes[arg][0]) == str:
            attributes[arg] = ["a"]
        else:
            attributes[arg] = []
    new_rel = Relation(name, attributes)
    # execute(new_rel.name)
    return new_rel


def rename(relation, old_name, new_name):
    """Fonction qui retourne une relation dont le name est la traduction du Renomage de SPJRUD en SQL,
    old_name est l'ancien nom d'attribut et new_name est le nouveau nom à attribuer
    PS: modifie aussi le attributes de la relatiion entrée en paramettre!!!
    """

    if not isarginrel(old_name, relation):
        raise AttributesError(f"{old_name} n'est pas un attribut de la relation {relation}")

    name = f"ALTER TABLE {relation.name} RENAME COLUMN {old_name} TO {new_name}"
    relation.attributes[new_name] = relation.attributes[old_name]
    del relation.attributes[old_name]
    new_rel = Relation(name, relation.attributes)
    # execute(new_rel.name)
    return new_rel
