from abc import ABC
from random import randint

# La classe NPC. On utilise python AbstractBaseClass
class NPC():
    # Initialiser a zero ou a vide
    force = 0
    agilite = 0
    constitution = 0
    intelligence = 0
    sagesse = 0
    charisme = 0
    classe_armure = 0
    nom = ""
    race = ""
    espece = ""
    point_vie = 0
    profession = ""

    # On recoit comme le parameter les valeurs que ne sont pas calcules
    def __init__(self, classe_armure, nom, race, espece, point_vie, profession):
        self.force = self.rouler_des()
        self.agilite = self.rouler_des()
        self.constitution = self.rouler_des()
        self.intelligence = self.rouler_des()
        self.sagesse = self.rouler_des()
        self.charisme = self.rouler_des()

        self.classe_armure = classe_armure
        self.nom = nom
        self.race = race
        self.espece = espece
        self.point_vie = point_vie
        self.profession = profession

    # Imprimer tous les champs
    def afficher_caracteristiques(self):
        print("nom:" + self.nom)
        print("race:" + self.race)
        print("espece:" + self.espece)
        print("point_vie:" + str(self.point_vie))
        print("profession:" + self.profession)
        print("classe_armure:" + self.classe_armure)
        print("force:" + str(self.force))
        print("agilite:" + str(self.agilite))
        print("constitution:" + str(self.constitution))
        print("intelligence:" + str(self.intelligence))
        print("sagesse:" + str(self.sagesse))
        print("charisme:" + str(self.charisme))


    # On jette le des 4 fois, et on somme le 3 plus grands
    def rouler_des(self):
        des = []
        for b in range(0, 4):
            des.append(randint(1, 6))
        des.sort(reverse=True)
        somme = des[0] + des[1] + des[2]
        return somme

    # Methode pour attaquer. Il est common pour Heros et Kobold
    def attaquer(self, cible):
        # je ne sais pas quoi envoyer comme le parametre
        cible.subir_dommage(self.force)

    # Methode pour subir dommage. Il est common pour Heros et Kobold
    def subir_dommage(self, quantite_domage):
        self.point_vie = self.point_vie - quantite_domage

# La classe pour Heros. Elle n'a pas rien de specifique, alors on appele la classe NPC
class Heros(NPC):
    def __init__(self, classe_armure, nom, race, espece, point_vie, profession):
        NPC.__init__(self, classe_armure, nom, race, espece, point_vie, profession)

# La classe pour Kobold. Elle n'a pas rien de specifique, alors on appele la classe NPC
class Kobold(NPC):
    def __init__(self, classe_armure, nom, race, espece, point_vie, profession):
        NPC.__init__(self, classe_armure, nom, race, espece, point_vie, profession)
