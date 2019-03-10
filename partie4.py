import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs")))
import getopt
import re
import difflib

#Script utilise pour representer les donnees dans le format demande en partie 4, point 2

def traitementStanFord() :
	reponse= ""
	fDonnees = open("wsj_0010_sample.txt.ner.stanford","r")
	previousElement = ""
	f2 = fDonnees.readlines()
	for paragraphe in f2:
		
		elements = paragraphe.split(" ")
		for element in elements:
			if('/ORGANIZATION' not in element and '/PERSON' not in element and '/LOCATION' not in element):
				print(element+": No organization or Location or Person")
				previousElement = ""
			else:
				print(element)
				mot_type = element.split("/")
				if(len(mot_type)>1):
					mot = mot_type[0]
					typ = mot_type[1]			
					if(previousElement == ""):
						previousElement = mot
						reponse = reponse+mot+"\t"+typ+"\t"+"0"+"\t"+"0(0/0)"+"\n"
					else:
						newElement = previousElement+" "+mot
						print(newElement)
						reponse = reponse.replace(previousElement,previousElement+" "+mot)
						previousElement = newElement	
					
						
				
	#on compte les occurences
	resultat = ""
	lignes = reponse.split("\n")
	compteur = 1
	for ligne in lignes:
		mots = ligne.split("\t")
		for mot in mots:
			if mot=="0":
				resultat=resultat+str(reponse.count(mots[0]))+"\t"
			elif mot=="0(0/0)" :
				resultat = resultat+"("+str(compteur)+"/"+str(len(lignes)-1)+")"
			else:
				resultat = resultat+mot+"\t"
		compteur = compteur+1
		resultat = resultat+"\n"			
	f = open("wsj_0010_sample.txt.ner.stanford.output","w+")
	f.write("Entite nommee\tType\tNombre d'occurence\tProportion dans le texte(%)\n"+resultat)
	f.close()
	fDonnees.close()



if __name__ == '__main__':
	traitementStanFord()
