from partie_2 import *
import os
import json

#QUESTION 15

def creer_partie(n): #Permet d'initialiser une partie
    plateau=creer_plateau(n)
    return {"joueur": 1, "plateau": plateau} #Cree un plateau puis retourn un dictionnaire contenant l'initialisation du joueur et le plateau

#QUESTION 16

def saisie_valide(partie, s): #Permet de savoir si la chaine permettant de poser un pion est valide
    tab=["a","b","c","d","e","f","g","h"] #initialise pour trouver une lettre
    if s=="M": #True du menu
        return True
    elif len(s)!=2: #False si la chaine contient plus de 2 caracteres
        return False
    
    elif s[0] not in tab or s[1] in tab: #False si pas entre a et h et si s[i] n'est pas un nombre
        return False
    
    elif case_valide(partie["plateau"],ord(s[0])-97, int(s[1])-1):
        if mouvement_valide(partie["plateau"],ord(s[0])-97, int(s[1])-1, partie["joueur"]):#Si la case est valide dans le tableau ET si un mouvement est posible
            return True
    return False

#QUESTION 17

def tour_jeu(partie): #Permet de placer le pion voulu à la case voulu et de retourner les pions qui peuvent l'etre
    os.system('cls') #Réinitialiser le terminal
    if partie["joueur"]==1:
        print("Tour du joueur: Noir")
    else:
        print("Tour du joueur: Blanc") #Afficher le joueur courant
        
    afficher_plateau(partie["plateau"]) #Affiche le plateau sur le terminal

    s=input("Entrer la case où vous voulez placer votre pion ou M pour accéder au menu: ")
    while saisie_valide(partie,s)==False: #Demander la chaine tant qu'elle est fausse
        s=input("Entrer la case où vous voulez placer votre pion ou M pour accéder au menu: ")

    if s=="M":
        return False
    
    indice_i=ord(s[0])-ord("a")
    indice_j=int(s[1])-1
    tab_temp=partie["plateau"]
    mouvement(partie["plateau"], indice_i, indice_j, partie["joueur"]) #Effectuer le mouvement à la position voulu
    return True
#QUESTION 18

def saisir_action(partie): #Affiche un menu
    print("Saisir:\n0 pour terminer le jeu\n1 pour commencer une nouvelle partie\n2 pour charger une partie\n")
    if partie is not None: #Si il y a une partie en cours
        print("3 pour Sauvegarder une partie en cours\n4 pour reprendre une partie en cours")
        x=int(input("Saisir votre choix: ")) #Demande du choix dans le cas ou il y a 4 propositions
        while x > 5 or x < 0: #S'assure que l'option choisis existe
            x=int(input("Saisir: 0 pour terminer le jeu\n        1 pour commencer une nouvelle partie\n        2 pour charger une partie\n        3 pour Sauvegarder une partie en cours\n        4 pour reprendre une partie en cours"))
        return x
    x=int(input("Saisir votre choix: "))
    
    while x > 2 or x < 0: #Idem mais avec 4 propositions
        x=int(input("Saisir: 0 pour terminer le jeu\n        1 pour commencer une nouvelle partie\n        2 pour charger une partie\n"))
        if x==2:
            if os.path.exists("sauvegarde_partie.json"):
                print("Il n'y a aucune partie sauvegarde\n\n")
                x=int(input("Saisir: 0 pour terminer le jeu\n        1 pour commencer une nouvelle partie\n        2 pour charger une partie\n"))
            
    return x

#QUESTION 19

def jouer(partie): #Permet de jouer une partie complete
    while not fin_de_partie(partie["plateau"]): #Tant que la partie n'est pas terminee
        if not(tour_jeu(partie)): #Si le joueur courant lance le menu, retourner faux
          return False
        if joueur_peut_jouer(partie["plateau"], pion_adverse(partie["joueur"])):
            partie["joueur"] = pion_adverse(partie["joueur"]) #Si l'adversaire peut jouer, changer le tour du joueur

    print(gagnant(partie["plateau"])) #Si la partie est terminé, un affiche qui a gagne
    return fin_de_partie(partie["plateau"])

#QUESTION 20

def saisir_taille_plateau(): #Permet au joueur de saisir la taille du plateau
    x=int(input("Saisir la taille du plateau (4,6,8): "))
    while x!=8 and x!=4 and x!=6: 
        x=int(input("Saisie invalide")) #Si la saisi du joueur est fausse, le jouer doit saisir une taille valide
    return x

#QUESTION 21

def sauvegarder_partie(partie): #Permet de sauvegarder une partie en cours
    with open('sauvegarde_partie.json', 'w') as f: 
        f.write(json.dumps(partie, indent=4)) #On ouvre le fichier voulu et on ecrit la partie courante dedans

#QUESTION 22

def charger_partie(): #Permet de reprendre une partie sauvegarde
    if os.path.exists("sauvegarde_partie.json"): #Si le fichier de sauvegarde existe
        with open('sauvegarde_partie.json', 'r') as f:
            partie = json.load(f) #On ouvre le fichier voulu et on copie son contenu dans la variable partie
            return partie 
    return 'Aucune partie enregistrée'

#Question23

def othello(): #Permet de jouer au jeu Othello en coordonnant les fonctions anterieurs
    choix=saisir_action(None)
    while True: #Tant que le joueur ne veut pas quitter le jeu
        if choix==0:
            return #arrête la fonction, donc le jeu
        elif choix==1: #Nouvelle partie
            n=saisir_taille_plateau()
            partie=creer_partie(n)
            jouer(partie)
        
        elif choix==2: #reprendre une partie sauvegarde
            partie=charger_partie()
            jouer(partie)
        elif choix==3: #Sauvegarde la partie courante
            sauvegarder_partie(partie)
        else: #Reprendre la partie voulu
            jouer(partie)
        choix=saisir_action(partie)
