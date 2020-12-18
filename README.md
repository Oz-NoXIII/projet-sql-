# projet-sql-

Outil de compilation (traduction) de requêtes SPJRUD vers des requêtes SQL

      Langage utilisé: Python

      Contributeurs: NYATCHO TONYA Frank
                     MUJYABWAMI Arsène
               
      Choix d'implémentation: 

                        a)Les relations sont définies par un objet Relation qui a deux attributs: un nom et un dictionnaire 
                        de listes de taille constante.
                        Nous avons fait ce choix car il facilite l'accès à la requête(le nom) et aux attributs de la relation.
                        
                        b)La selection est une fonction à 5 paramètres: 1.La relation qui est une instance de Relation;
                        
                                                                        2.L'attribut qui doit être un attribut (clé du dictionnaire)
                                                                        de la relation;
                                                                        
                                                                        3.Le comparateur qui doit faire partie de la liste
                                                                        prédéfini de symboles: '=', '<', '>', '<=', '>=' ou '!='
                                                                        
                                                                        4.La valeur à comparer qui peut être un attribut de la relation ou une constante
                                                                        si c'est une constante, cette valeur doit être du même type que ceux des valeurs de l'attribut 
                                                                        si c'est un attribut, elle doit être un attribute de la relation (clé du dictionnaire);
                                                                        
                                                                        5.Le compteur qui indique si la valeur à comparer est un
                                                                        attribut (clé du dictionnaire) de la relation ou une constante.
                                                                        si counter != 1 alors la valeur à comparer est une constante
                                                                        si counter = 1 alors la valeur à comparer est un attribut de la relation
                                                                         
                        c)La projection est une fonction à paramètres variables: 1.La relation;
                                                                                  ***les attributs qui doivent être des 
                                                                                  clés du dictionnaire(supprime les doublons)
                          
                        d)La jointure est une fonction à 2 paramètres: deux relations de mêmes attributs.
              
                          
                        e)Le renommage est une fonction à 3 paramètres: 1.La relation dans laquelle l'action aura lieu;
                                                                         2.L'ancien nom de l'attribut;
                                                                         3.Le nouveau nom de l'attribut;
                                                                        
                        f)L'union est une fonction à 2 paramètres: deux relations de mêmes attributs.
                          (supprime les doublons)
                          
                        g)La différence sera une fonction à 2 paramètres: deux relations de mêmes attributs.
                        
                        h)L'exécution et l'affichage du resultat d'un requête peut se faire de deux manières:
                         - Soit en créant d'abord une nouvelle table à partir du resultat d'une requête avec la fonction SPJRUDtoSQL.create() et ensuite afficher le resultat avec la fonction SPJRUDtoSQL.display().
                         - Soit en affichant directement le resultat de la requête sans créer la table en BD avec la fonction SPJRUDtoSQL.create().
                        
                        i)La création d'une table peut se faire par l'intermediaire d'un nom et d'un dictionnaire 
                        (fonction relation()) ou par l'intermédiaire d'un nom et d'une instance de relation c-à-d une requête.
                        
      Explication:
      
                        Pour utiliser cet outil de compilation (traduction) de requêtes SPJRUD vers des requêtes SQL, 
                        il suffit d'utiliser le module SPJRUDtoSQL qui contient 9 fonctions différentes: 
                        une fonction pour chaque opérateur unitaire ou binaire, une fonction display() pour l'affichage,
                        une fonction create() pour la création d'une table à partir du résultat d'une requête et une fonction relation() pour 
                        la definition d'une relation avec un nom et un dictionnaire python.
                        
                        Les requêtes imbriquées sont permises. (exemple: 
                        SPJRUDtoSQL.project((
                        SPJRUDtoSQL.select(
                        SPJRUDtoSQL.join(rel1, rel2),
                        "=", 'B', 3, 0)), # paramètres de la sélection
                        'A') # paramètre de la projection
                        est la projection de A sur la selection où B=3 sur la jointure de la relation 1 avec la relation 2)
                        
                       
         
      Difficultées:
      
                        La répartition des tâches a été un vrai défi tout comme la communication en générale et cela est surtout
                        dû aux circonstances exceptionnelles dans lesquelles nous nous trouvons actuellement, mais aussi par la 
                        découverte du projet le mois passé qui suivait justement la fin d'un autre projet d'un autre cours.
                        
               
--------------------------------------------------------------------------------------------------------------------------------------------------
      Exemples d'utilisation des differents operateurs:
      
        Tout d'abors importer le module SPJRUDtoSQL
      
      
      1) Selection:
      
      name = "nom_relation" # Nom de la relation
      attributes = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]} # Attributs de la relation
      rel = SPJRUDtoSQL.relation(name, attributes) # Création de la relation
      requete = SPJRUDtoSQL.select(rel, "=", "d", "b", 0) # Operation de selection retournant la requette SQL
      SPJRUDtoSQL.create("selection", requete) # Création d'une nouvelle table a partir du resultat de la requette
      SPJRUDtoSQL.display("selection") # Affichage du resultat de l'opération à l'ecran
      
      
      2) Projection:
      
          name = "nom_relation" # Nom de la relation
          attributes = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]} # Attributs de la relation
          rel = SPJRUDtoSQL.relation(name, attributes) # Création de la relation
          requete = SPJRUDtoSQL.project(rel, "d", "b", "a") # Operation de projection retournant la requette SQL
          SPJRUDtoSQL.create("projection", requete) # Création d'une nouvelle table a partir du resultat de la requette
          SPJRUDtoSQL.display("projection") # Affichage du resultat de l'opération à l'ecran
      
      
      3) Renommage
        
          name = "nom_relation" # Nom de la relation
          attributes = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]} # Attributs de la relation
          rel = SPJRUDtoSQL.relation(name, attributes) # Création de la relation
          requete = SPJRUDtoSQL.project(rel, "d", "b", "a") # Operation de projection retournant la requette SQL
          SPJRUDtoSQL.create("renommage", requete) # Création d'une nouvelle table a partir du resultat de la requette
          SPJRUDtoSQL.display("renommage") # Affichage du resultat de l'opération à l'ecran
          
          
      3) Jointure
        
          attri1 = {"A": [1, 1, 2, 2], "B": [3, 4, 4, 3], "C": [5, 5, 5, 6]}
          rel1 = SPJRUDtoSQL.relation("rel1", attri1)
          attri2 = {"C": [5, 5, 5, 6], "D": [2, 2, 1, 1], "B": [3, 4, 4, 4]}
          rel2 = SPJRUDtoSQL.relation("rel2", attri2)
          
          requete = SPJRUDtoSQL.join(rel1, rel2) # Operation de Jointure retournant la requette SQL
          SPJRUDtoSQL.create("jointure", requete) # Création d'une nouvelle table a partir du resultat de la requette
          SPJRUDtoSQL.display("jointure") # Affichage du resultat de l'opération à l'ecran
        
      
      3) Union
        
         attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
         rel1 = SPJRUDtoSQL.relation("rel1", attri1)
         attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
         rel2 = SPJRUDtoSQL.relation("rel2", attri2)
         
         requete = SPJRUDtoSQL.union(rel1, rel2)
         SPJRUDtoSQL.create("union", requete)
         SPJRUDtoSQL.display("union")
         
         
      4) Difference
        
         attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
         rel1 = SPJRUDtoSQL.relation("rel1", attri1)
         attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
         rel2 = SPJRUDtoSQL.relation("rel2", attri2)
         
         requete = SPJRUDtoSQL.difference(rel1, rel2)
         SPJRUDtoSQL.create("difference", requete)
         SPJRUDtoSQL.display("difference")
          