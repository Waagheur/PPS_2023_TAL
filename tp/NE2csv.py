import sys
import os

if (len(sys.argv) < 3):
    print("Not enough parameters, should be : NE2csv.py source output")
    
else:
    sum = 0
    store = {}
    
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                
                pair = line.split('\t')

                if (len(pair) == 2):
                    sum += 1
                    
                    if (line in store.keys()):
                        store[line] += 1
                    else:
                        store[line] = 1
            
            w.write("Entité nommée,Type,Nombre d'occurrences,Proportion dans le texte (%)\n")
            
            for key, value in store.items():
                pair = key.split('\t')
                w.write(pair[0] + ',' + pair[1].split('\n')[0] + ',' + str(value) + ',' + str(value/sum*100) + '\n')
