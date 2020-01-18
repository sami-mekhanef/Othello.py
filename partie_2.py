from partie_1 import *

###QUESTION 7

def pion_adverse(joueur): #Permet d'avoir le chiffre du pion adverse
    assert joueur==1 or joueur==2
    if joueur==1:
        return 2
    return 1

#QUESTION 8

def prise_possible_direction(plateau, i, j, vertical, horizontal, joueur): # Prends en paramètre un plateau, un indice i et un indice j, une direction vertical, une direction horizontal et un identifiant de joueur renvoit True si au moins un pion est "mangé" si le joueur pose le pion en (i,j)
  if case_valide(plateau, i, j) and case_valide(plateau, i+vertical, j+horizontal) and get_case(plateau, i+vertical, j+horizontal) == pion_adverse(joueur): #Si la case adjacente existe et contient un pion adverse
    dirvertical = vertical
    dirhorizontal = horizontal
    pion_suivant = get_case(plateau, i+dirvertical, j+dirhorizontal) 
    while pion_suivant == pion_adverse(joueur) and case_valide(plateau, i+dirvertical, j+dirhorizontal): #Tant que le pion suivant est valide et contient un pion adverse
      pion_suivant = get_case(plateau, i+dirvertical, j+dirhorizontal)
      dirvertical += vertical # Avance dans la direction vertical
      dirhorizontal += horizontal # Avance dans le direction horizontal
    return joueur == pion_suivant
  return False

#QUESTION 9

def mouvement_valide(plateau,indice_i,indice_j,joueur): #Permet de savoir si des cases autour de la case choisie peuvent être prise
    if get_case(plateau,indice_i,indice_j)!=1 and get_case(plateau,indice_i,indice_j)!=2 : #Contourne le assert 
        verticale=-1 
        while verticale<2 and case_valide(plateau, indice_i, indice_j): #On initialise -1 afin de faire en sorte que verticale soit = à -1 , 0 et 1
            horizontale=-1
            while horizontale<2 : #idem
                if case_valide(plateau, indice_i+verticale, indice_j+horizontale) and prise_possible_direction(plateau,indice_i,indice_j,verticale,horizontale,joueur):
                    return True #Pendant cette boucle, si une prise est possible, on return True
                horizontale+=1
            verticale+=1
    return False
    

#QUESTION 10

def mouvement_direction(plateau,indice_i,indice_j,verticale,horizontale,joueur): #Permet de retourner les cases pouvant être prise
    if mouvement_valide(plateau,indice_i,indice_j,joueur) and case_valide(plateau, indice_i+verticale, indice_j+horizontale): #On s'assure qu'il y a des cases pouvant être prises
        temp_v=verticale
        temp_h=horizontale
        if prise_possible_direction(plateau,indice_i,indice_j,verticale,horizontale,joueur):
            while prise_possible_direction(plateau,indice_i,indice_j,verticale,horizontale,joueur)!=False and case_valide(plateau, indice_i+verticale, indice_j+horizontale):
                set_case(plateau,indice_i+verticale,indice_j+horizontale,joueur)
                set_case(plateau,indice_i,indice_j,joueur) #Tant que la case peut etre prise, on prend la case de départ et la case prise ##!!
                verticale+=temp_v
                horizontale+=temp_h
            set_case(plateau,indice_i+verticale,indice_j+horizontale,joueur) #à la fin, si le mouvement est possible, on "retourne" également la case 0 à joueur
    return plateau

#QUESTION 11

def mouvement(plateau, indice_i, indice_j, joueur): #Mouvement_direction mais dans toutes les directions
    verticale=-1
    while verticale<2 and case_valide(plateau, indice_i, indice_j): #Comme pour la fonction mouvement valide
        horizontale=-1
        while horizontale<2:
            if case_valide(plateau, indice_i+verticale, indice_j+horizontale):
                mouvement_direction(plateau,indice_i,indice_j,verticale,horizontale,joueur) #idem
            horizontale+=1
        verticale+=1
            
    
#QUESTION 12

def joueur_peut_jouer(plateau, joueur): #Permet de savoir si la partie continue
    i=0
    while i<len(plateau["cases"]):
        j=0
        while j<len(plateau["cases"]):
            if not mouvement_valide(plateau, i, j, joueur):
                return True
            j+=1
        i+=1
    return False
        

#QUESTION 13

def fin_de_partie(plateau): #permet de savoir si la partie est terminée
    if joueur_peut_jouer(plateau,1)==True and joueur_peut_jouer(plateau,2)==True:
        return False
    return True #Si la fonction joueur_peut_jouer est vraie la partie continue, dans le cas contraire la partie est terminée
        

#QUESTION 14

def gagnant(plateau): #Permet de savoir qui a gagné
    b=0 #Blanc
    n=0 #Noir
    i=0
    while i<len(plateau["cases"]): #boucle pour compter le nombre de blanc et de noir
        if plateau["cases"][i]==2:
            b+=1
        elif plateau["cases"][i]==1:
            n+=1
        i+=1 
    if b>n: #Si plus de blanc alors blanc gagne 
        return 2
    elif b<n: #Si plus de noir alors noir gagne
        return 1
    return 0 #Si le score est le même on retourne 0
