----- pos2txt.py -----

Programme pour convertir un fichier de pos tags au format :
	Pierre Vinken	PROPN
	,	COMMA
en un fichier texte normal :
	Pierre Vinken,
	
commande : 
	python pos2txt.py source output
source : le chemin vers le fichier annoté
output : le chemin du fichier dans lequel sera écrit le texte normal
ex : python pos2txt.py ../data/pos_reference.txt ../data/pos_test.txt

----- nltkPosTagging.py -----

Programme pour annoter un texte avec des POS tags nltk:
	Not this
	=>
	Not	RB
	this	DT

commande : 
	nltkPosTagging.py source output
source : le chemin vers le fichier texte à annoter
output : le cheming du fichier dans lequel sera écrit la version annotée du texte
ex : python nltkPosTagging.py ../data/wsj_0010_sample.txt ../data/wsj_0010_sample.txt.pos.nltk

----- stanfordPosTagging.py -----

Programme pour annoter un texte avec des POS tags stanford:
	Not this
	=>
	Not	RB
	this	DT

commande : 
	stanfordPosTagging.py source output
source : le chemin vers le fichier texte à annoter
output : le cheming du fichier dans lequel sera écrit la version annotée du texte
ex : python stanfordPosTagging.py ../data/wsj_0010_sample.txt ../data/wsj_0010_sample.txt.pos.stanford

Note : stanfordPosTagging est plus lent que nltkPosTagging

----- nltk2univ.py -----

Programme pour convertir un fichier POS tags nltk au format :
	Not	NOT
	this	DT
en un fichier POS tags au format universel :
	Not	ADV
	this	DET
avec l'aide d'un dictionnaire au format:
	CC  CONJ
	CD  NUM
	DT  DET

commande : 
	python nltk2univ.py source dict output
source : le chemin vers le fichier POS tags nltk
dict : le chemin vers un fichier de dictionnaire de POS tags de nltk à univ
output : le chemin du fichier dans lequel sera écrit le fichier POS tags universel
ex : python nltk2univ.py ../data/wsj_0010_sample.txt.pos.nltk ../data/POSTags_PTB_Universal.txt ../data/wsj_0010_sample.txt.pos.univ

----- ref2univ.py -----

Programme pour convertir un fichier POS tags REF au format :
	Pierre Vinken	PROPN
	,	.
	61 years old	ADJ
en un fichier POS tags au format universel :
	Pierre Vinken	NOUN
		
	,	.
	61 years old	ADJ
		
		

commande :
	python ref2univ.py source dictREF2PTB dictPTB2UNIV output
source : le chemin vers le fichier POS tags REF
dictREF2PTB : le chemin vers un fichier de dictionnaire de POS tags de REF à PTB
dictPTB2UNIV : le chemin vers un fichier de dictionnaire de POS tags de PTB à univ
output : le chemin du fichier dans lequel sera écrit le fichier POS tags universel
ex : python ref2univ.py ../data/pos_reference.txt ../data/POSTags_REF_PTB.txt ../data/POSTags_PTB_Universal.txt ../data/pos_reference.txt.univ

----- conll2txt.py -----

Programme pour convertir un fichier conll au format :
	Mary	B-PER	
	Barra	I-PER	
en un fichier texte normal :
	Mary Barra
	
commande : 
	python conll2txt.py source output
source : le chemin vers le fichier conll
output : le chemin du fichier dans lequel sera écrit le texte normal
ex : python conll2txt.py ../data/ne_reference.txt.conll ../data/ne_test.txt

----- nltkNE.py -----

Programme pour extraire les entités nommées d'un fichier texte à l'aide de nltk

commande : 
	python nltkNE.py source output
source : le chemin vers le fichier texte où extraire les entitées nommées
output : le chemin du fichier dans lequel sera écrit les entités nommées trouvées
ex : python nltkNE.py ../data/wsj_0010_sample.txt ../data/wsj_0010_sample.txt.ne.nltk

----- stanfordNE.py -----

Programme pour extraire les entités nommées d'un fichier texte à l'aide de stanford

commande : 
	python stanfordNE.py source output
source : le chemin vers le fichier texte où extraire les entitées nommées
output : le chemin du fichier dans lequel sera écrit les entités nommées trouvées
ex : python stanfordNE.py ../data/wsj_0010_sample.txt ../data/wsj_0010_sample.txt.ne.stanford

Note : stanfordNE est plus lent que nltkNE

----- nltkNE2conll.py -----

Programme pour convertir un fichier d'entités nommées nltk au format :
	Boca Raton	PERSON
	Hot Springs	PERSON
en un fichier d'entités nommées au format conll :
	Boca	B-PERS
	Raton	I-PERS
	Hot	B-PERS
	Springs	I-PERS

commande : 
	python nltkNE2conll.py source dict output
source : le chemin vers le fichier POS tags nltk à convertir
output : le chemin du fichier dans lequel sera écrit le fichier d'entitées nommées conll
ex : python nltkNE2conll.py ../data/wsj_0010_sample.txt.ne.nltk ../data/wsj_0010_sample.txt.ne.nltk.conll

----- customEvaluate.py -----

Programme pour evaluer la précision et le rappel
Les deux fichiers à comparer doivent compter le même nombre de ligne et utiliser le format :
	MOT	TAG
	MOT2	TAG2
avec les mêmes mots et les mêmes types de tags pour avoir des résultats cohérents

commande :
	python customEvaluate.py reference comparison
reference : le chemin vers le fichier de référence
comparison : le chemin verss le fichier avec lequel comparer la référence
ex : python customEvaluate.py ../data/ne_reference.txt.conll ../data/ne_test.txt.ne.nltk.conll

----- evaluate.py -----

Programme d'évaluation, retourne des résultats incohérents, non utilisé pour analyse