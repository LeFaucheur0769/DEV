############################
############################
#	les variables fixes	   #
############################
############################

min = 8000 ##taille minimale de la clef
max = 80000	##taille maximale de la clef
hex = True ##variable pour verifier si c'est en hexadécimale

#############################
#############################
#	les modules a importer	#
#############################
#############################
import random ##importe le module random pour avoir des nombres pseudo aléatoire
 
boucle = 0 ## définis une varible pour le nombre de tours de cryptage a faire

while(boucle >= random.randint(100, 1000)):
	first = random.randint(1, 1250) ## Defini le premier nombre aléatoire (a mettre en hexadécimale)
