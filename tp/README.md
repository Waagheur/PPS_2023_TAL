----- conll2pos.py -----

Programme pour découper un fichier colonne annoté au format :
	0	.	.	PONCTU	SENT	_	_	1	Dummy	_	_
	1	Not	not	ADV	NOT	_	_	2	Dummy	_	_
	2	this	this	DET	DT	_	_	3	det	_	_
en un fichier de POS tags au format :
	Not	NOT
	this	DT

commande : 
	python conll2pos.py source output
source : le chemin vers le fichier colonne à découper
output : le chemin du fichier dans lequel sera écrit le texte à annoter
ex : python conll2pos.py ../data/wsj_0010_sample.txt.conll ./wsj_0010_sample.txt.pos

----- conll2txt.py -----

Programme pour découper un fichier colonne annoté au format :
	0	.	.	PONCTU	SENT	_	_	1	Dummy	_	_
	1	Not	not	ADV	NOT	_	_	2	Dummy	_	_
	2	this	this	DET	DT	_	_	3	det	_	_
en un fichier de texte à annoter au format :
	Not this
	
commande : 
	python conll2txt.py source output
source : le chemin vers le fichier colonne à découper
output : le chemin du fichier dans lequel sera écrit le texte à annoter
ex : python conll2txt.py ../data/wsj_0010_sample.txt.conll ./wsj_0010_sample.txt

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
ex : python nltk2univ.py ../data/wsj_0010_sample.txt.pos.nltk ../data/POSTags_PTB_Universal_Linux.txt ./wsj_0010_sample.txt.pos.univ

----- nltkChunks.py -----

Programme pour extraire les mots composés d'un texte à l'aide de nltk
et d'un fichier de règles de grammaire au format :
	Determinant-Adjectif-Nom:Determinant-Adjectif-Nom: {<DT>?<JJ>*<NN>}

commande : 
	python nltkChunks.py source grammar output
source : le chemin vers le fichier texte où extraire les mots composés
grammar : le chemin vers un fichier de règles de grammaire
output : le chemin du fichier dans lequel sera écrit le fichier de mots composés
ex : python nltkChunks.py ../data/wsj_0010_sample.txt ../data/grammar ./wsj_0010_sample.txt.chk.nltk

----- nltkNE.py -----

Programme pour extraire les entités nommées d'un fichier texte à l'aide de nltk

commande : 
	python nltkNE.py source output
source : le chemin vers le fichier texte où extraire les entitées nommées
output : le chemin du fichier dans lequel sera écrit les entités nommées trouvées
ex : python nltkNE.py ../data/wsj_0010_sample.txt ./wsj_0010_sample.txt.ne.nltk

----- nltkNE2univ.py -----

Programme pour convertir un fichier d'entités nommées nltk au format :
	Boca Raton	PERSON
	Hot Springs	PERSON
en un fichier d'entités nommées au format universel :
	Boca Raton	PER
	Hot Springs	PER
avec l'aide d'un dictionnaire au format:
	LOCATION   LOC
	ORGANIZATION   ORG

commande : 
	python nltkNE2univ.py source dict output
source : le chemin vers le fichier POS tags nltk à convertir
dict : le chemin vers un fichier de dictionnaire d'entitées nommées de nltk à univ
output : le chemin du fichier dans lequel sera écrit le fichier d'entitées nommées universel
ex : python nltkNE2univ.py ../data/wsj_0010_sample.txt.ne.nltk ../data/NERTags_PTB_Universal_Linux.txt ./wsj_0010_sample.txt.ne.univ

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