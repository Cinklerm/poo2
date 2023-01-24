from NPC import NPC, Heros, Kobold


m = Heros("arm", "martin cinkler", "ork", "homo", 50, "etudiant")
monstre = Kobold("armoure", "nessie", "dino", "reptile", 50, "monstre lacustre")

m.afficher_caracteristiques()
print("==================")
monstre.afficher_caracteristiques()
print("==================")
m.attaquer(monstre)
print("======== apres l'attaque ==========")
monstre.afficher_caracteristiques()
