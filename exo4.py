import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs")))
import getopt
import re
import difflib

#Remplace par le tag universel
def refTag(oldTag):
	#pretraitement pour enlever les caractères invisibles
	oldTag = oldTag.replace(' \n','')
	oldTag = oldTag.replace('\n','')

	#on ouvre la table de correspondance
	fTags = open("POSTags_PTB_Universal.txt","r")
	fLines = fTags.readlines()
	#bug avec CC : on le traite à part
	if(oldTag == "CC"):
		return "CONJ"

	#pour chaque ligne de la table de correspondance
	for line in fLines:
		tags = line.split(" ")
		if(len(tags)>1):
			#si des elements vides se sont glissés on les enleves
			if(len(tags)>2):
				tags = filter(None,tags);
			#le tag PTB correspond a notre tag : on renvoie le tag uni correspondant
			if(oldTag == tags[0]):
				tags[1] = tags[1].replace('\r\n','')
				return tags[1]
	return oldTag

#traitement pour wsj_0010_sample.txt.pos.lima -> wsj_0010_sample.txt.pos.univ.lima
def traitementLima() :
	reponse=""
	fDonnees = open("wsj_0010_sample.txt.pos.lima","r")
	f2 = fDonnees.readlines()
	motsTags = f2[0].split(" ")
	#on decoupe en elements mot_tag
	for motTag in motsTags:
		#on separe le tag du mot
		sp = motTag.split("_")
		if(len(sp)>1):
			mot = sp[0]
			tag = sp[1]
			#on met dans le resultat final le mot avec le nouveau tag
			reponse = reponse+mot+"_"+refTag(tag)+" "
				
	#on ecrit le nouveau fichier avec la reponse
	f = open("wsj_0010_sample.txt.pos.univ.lima","w+")
	f.write(reponse)
	f.close()
	fDonnees.close()
		
#traitement pour wsj_0010_sample.txt.pos.stanford -> wsj_0010_sample.txt.pos.univ.stanford
def traitementStanFord() :
	reponse=""
	fDonnees = open("wsj_0010_sample.txt.pos.stanford","r")
	f2 = fDonnees.readlines()
	for paragraphe in f2:
		motsTags = paragraphe.split(" ")
		for motTag in motsTags:
			sp = motTag.split("_")
			if(len(sp)>1):
				mot = sp[0]
				tag = sp[1]
				reponse = reponse+" "+mot+"_"+refTag(tag)
		reponse = reponse+"\n"
				
					
	f = open("wsj_0010_sample.txt.pos.univ.stanford","w+")
	f.write(reponse)
	f.close()
	fDonnees.close()

#traitement pour wsj_0010_sample.txt.pos.ref -> wsj_0010_sample.txt.pos.univ.ref
def traitementLima2():
	reponse=""
	myFile = open("wsj_0010_sample.txt.pos.ref","r")
	f1 = myFile.readlines()
	#on separe chaque ligne (ligne = mot \t tagPTB)
	for line in f1:
		sp = line.split("\t")
		 #on enregistre avec a la place de tagPTB -> tagUniv 
		reponse = reponse+sp[0]+"\t"+refTag(sp[1])+"\n"
	#on sauvegarde le resultat dans un nouveau fichier
	f = open("wsj_0010_sample.txt.pos.univ.ref","w+")
	f.write(reponse)
	f.close()
	myFile.close()

	

if __name__ == '__main__':
	traitementLima()
	traitementLima2()
	traitementStanFord()
