import sys
import os
from nltk import RegexpParser
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

if (len(sys.argv) < 4):
    print("Not enough parameters, should be nltkChunks.py source grammar output")
    
else:
    with open(sys.argv[2], "r") as dic:
        grammar = {}
        for line in dic.readlines():
            pair = line.split(':')
            grammar[pair[0]] = pair[1]
    grammar = {"Determinant-Adjectif-Nom":"Determinant-Adjectif-Nom: {<DT>?<JJ>*<NN>}",
            "Adjectif-Nom":"Adjectif-Nom: {<JJ><NN>}",
            "Nom-Nom":"Nom-Nom: {<NN><NN>}",
            "Adjectif-Nom-Nom":"Adjectif-Nom-Nom: {<JJ><NN><NN>}",
            "Adjectif-Adjectif-Nom":"Adjectif-Adjectif-Nom: {<JJ><JJ><NN>}"}

    with open(sys.argv[1], "r") as f:
        with open(sys.argv[3], "w") as w:
            lines = "";
            for line in f.readlines():
                lines += " " + line;
                
            tokens = word_tokenize(lines)

            tags = nltk.pos_tag(tokens)
        
            for element, rule in grammar.items():

                w.write(element + " : \n")
                
                chunker = RegexpParser(rule)
                
                entries = str(chunker.parse(tags)).split(element)[1:]
                entries2 = []
                for e in entries:
                    entries2.append(e.split(")")[0][1:])
                    
                # print(entries2)
                    
                entries3 = []
                for e in entries2:
                    entries3 = []
                    sub = e.split("/")
                    entries3.append(sub[0])
                    
                    for word in sub[1:-1]:
                        entries3.append(word.split(" ")[1])
                        # entries3.append(word.split(" "))
                    
                    for i, e in enumerate(entries3):
                        if (i != 0):
                            w.write(" ")
                        w.write(e)
                    
                    w.write("\n")

                w.write("\n")