import random
import time



def lancer_un_dé(nombre_de_faces = 6):
    d = random.randint(1,nombre_de_faces)
    return d

def lancer_deux_dés(nombre_de_dé = 2, nombre_de_faces = 6):
    somme_des_dé = 0
    #liste_de_de = []
    for i in range (nombre_de_dé):
        d = lancer_un_dé()
        #liste_de_de.append(d)
        somme_des_dé += d
    return somme_des_dé


# génération d'une liste avec un contenu signé aléatoire 
def plateau (nb_cases):
    liste = []
    for i in range(nb_cases):
        a = random.randint(-10,10)
        liste.append(a)
    return liste



a=0
b=0
position_initial_pion = {'J1': a, 'J2': b}

while 1:

    # changement de la key du dictionnaire en fonction du résultat du lancé de dé
    result = lancer_deux_dés()
    print ('le résultat du lancé est:', result) 
    position_initial_pion['J1'] += result
    print ('position après lancer:', position_initial_pion['J1'])
    time.sleep(3)




