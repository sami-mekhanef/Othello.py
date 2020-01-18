from termcolor import colored, cprint
from colorama import *
init ()



#Question 1

def indice_valide(plateau,indice):
    return indice<plateau["n"] and indice>=0

#Question 2

def case_valide(plateau,indice_i,indice_j):
    return indice_valide(plateau,indice_i) and indice_valide(plateau,indice_j)
    

    


#Question 3

def get_case(plateau,indice_i,indice_j):
    assert case_valide(plateau,indice_i,indice_j)
    return plateau["cases"][indice_i*plateau['n']+indice_j]

    
#Question 4


def set_case(plateau,indice_i,indice_j,val):
        assert  val>0 and val<=2 and get_case(plateau,indice_i,indice_j)==0 or get_case(plateau,indice_i,indice_j)==1 or get_case(plateau,indice_i,indice_j)==2
        insert=plateau["cases"][plateau["n"]*indice_i+indice_j]=val


#Question 5

def creer_plateau(n):
    plateau={}
    cases=[]
    assert (n==4 or n==6 or n==8)
    i=0
    while i<n*n:
        cases.append(0)
        i+=1
    centre=len(cases)//2
    milieu=centre-(n//2)
    cases[milieu]=1
    cases[milieu-1]=2
    cases[milieu+n]=2
    cases[milieu+n-1]=1
    plateau["n"]=n
    plateau["cases"]=cases
    return plateau

#Question 6

def afficher_plateau(plateau): # Prend en paramètre un plateau et affiche le plateau de jeu
  c = 1 # la variable c correspond au parcours des cases
  bordureh = "     "  # Initialisation de la bordure supérieur
  ligne1 = ""         # Initialisation des lignes impaires
  ligne2 = ""         # Initialisation des lignes paires
  while c < plateau["n"]+1: # Permet de crée les lignes paires (ligne2) et impair (ligne1) du plateau
      if c%2 != 0: 
        ligne1 += colored("       ", None, "on_magenta")
        ligne2 += colored("       ", None, "on_cyan")
      else:
        ligne1 += colored("       ", None, "on_cyan")
        ligne2 += colored("       ", None, "on_magenta")
      bordureh += str(c).ljust(7)
      c += 1
  print(bordureh) #affiche les indices de case horizontaux (1,2,3,4...)
  
  i = 0
  while i < plateau["n"]: # Affiche la plateau cases par cases
    ligne_milieu = (chr(97+i).ljust(2)) #indice verticale (a, b, c, d,...), mais aussi la ligne qui contiendra le pion
    j = 0
    while j < plateau["n"]:
      pion = str(get_case(plateau, i, j)) 
      if  pion == "2":  #Si le pion sur la case est blanc
        couleur_pion = 'white'
        pion = pion.replace("2", "###")
      elif pion == "1": #Si le pion sur la case est noir
        couleur_pion = 'grey'
        pion = pion.replace("1", "###")
      else:            #Si la case est vide
        couleur_pion = None
        pion = pion.replace("0", "   ")
        
      if i%2 == j%2:      #Test si les 2 indices (i,j) sont dans le même état (paires ou impaires)
        couleur = 'on_magenta'
      else: 
        couleur = 'on_cyan'

      ligne_milieu += colored("  " + str(pion) + "  ", couleur_pion, couleur)
      j += 1

    if i%2 == 0: # Si i est pair affiche les lignes pairs, sinon affiche les lignes impairs
      print("  " + str(ligne1) + "\n" + str(ligne_milieu)  + "\n  " + str(ligne1))
    else:
      print("  " + str(ligne2) + "\n" + str(ligne_milieu)  + "\n  " + str(ligne2))
    i += 1
