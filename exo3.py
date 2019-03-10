import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs")))
import getopt
import re


def conllToMotEtiq():
	resultat = ""
	f = open("wsj_0010_sample.txt.conll","r")
	f1 = f.readlines()
	for x in f1 :

		ligne = re.split(r'\t+',x)
		if(len(ligne) >3):
			mots = ligne[1].split(" ")
			for mot in mots:
				if(ligne[4] == "SENT"):
					ligne[4] = "."
				elif(ligne[4] == "COMMA"):
					ligne[4]= ","
				resultat = resultat+mot+"_"+ligne[4]+" "
	fileDest = open("wsj_0010_sample.txt.pos.lima","w")
	fileDest.write(resultat)
	f.close()
		

    
if __name__ == '__main__':
   conllToMotEtiq()
