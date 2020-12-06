import fct_utile
from fct_utile import ErrorType,NumberRelationError,AttributesError,isarelation


def join(rel1, rel2):
    """Fonction qui retourne le str qui est la traduction de la jonction en SPJRUD en SQL"""

    if fct_utile.joinable(rel1, rel2):
        sol = f"select * from {rel1.nom} natural join {rel2.nom}"
    else:
        raise fct_utile.ErrorKey("Jonction impossible car aucun attribut en commun")
    return sol


def union(*relations):
    # if(more_than_one_realtion(*rel)):
    #     pass
    #
    # query = ""
    # item_query=[]
    # for index, rel in enumerate(relations):
    #     item_query[index]=f"SELECT * FROM {rel.nom}"
    #
    # for item in item_query:
    #     query = f"UNION {item}"
    pass  # TODO

"""
Fonction qui retourne True si les relations passées en paramètres ont les(même nom,et attributs de même type) et sinon retourne False 
"""
def same_oder_attributes(*relations):
    pass

"""
Fonction qui retourne True si les relations passées en paramètres sont identiques(même nom,et attributs de même type et d'ordre) et sinon retourne False
"""
# def same_attributes(*relations:Relation):
#     if are_a_relation(*relations) and more_than_one_relation(*relations) and same_number_attributes(*relations):
#         for attribut in relations.dicos:
#             for key, val in attribut:
#                 if key in type(relations[0].dico)


def same_name(*relations):
    result = False
    if are_a_relation(*relations) and more_than_one_relation(*relations) and same_number_attributes(*relations):
        for rel in relations:
            if relations[0].name == rel.name:
                result = True
            else:
                raise ErrorType(f"Les relations {relations} n'ont pas les même noms d'attributs")
                result = False

"""
Fonction qui retourne True les paramètres passés sont des Relations et sinon retourne False
"""
# def are_a_relation(*relations):
#     result = False
#     for rel in relations:
#         if rel.name and type(rel.name)==str and rel.dicos and type(rel.dicos)==dict:
#             result = True
#         else:
#             raise ErrorType(f"Le paramètre {rel} n'est pas une relation valide")
#             result = False
#             break
#     return result

def are_a_relation(*relations):
    result = False
    for rel in relations:
        if isarelation(rel):
            result = True
        else:
            result = False
            break

    return result

"""
Fonction qui retourne True si les relations passées en paramètres ont le même nombre d'attributs et sinon retourne False 
"""
def same_number_attributes(*relations):
    result = False
    if are_a_relation(*relations) and more_than_one_relation(*relations) :
        length=len(relations[0].dicos)
        result=True
        for rel in (relations):
            if len(rel.dicos)!=length:
                raise AttributesError(f"Les relations {relations} n'ont pas le meme même d'attributs")
                result=False
                break
    return result

"""
Fonction qui retourne True s'il ya au moins deux relations passées en paramètres et sinon retourne False 
"""
def more_than_one_relation(*relations):
    if len(relations)<2:
        raise NumberRelationError("Au moins deux relations nécessaires pour cette opération")
        return False
    else:
        return True


def difference(rel1, rel2):
    """Fonction qui retourne le str qui est la traduction de la différence en SPJRUD en SQL"""

    if fct_utile.havesameargs(rel1, rel2):
        sol = f"select * from {rel1.nom} except select * from {rel2.nom}"
    else:
        raise fct_utile.ErrorKey(f"Différence impossible car attributs de {rel1.nom} différent de {rel2.nom} ")
    return sol
