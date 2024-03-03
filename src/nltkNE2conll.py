import sys
import os

if (len(sys.argv) < 3):
    print("Not enough parameters, should be nltkNE2conll.py source output")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                if (line == "\n"):
                    w.write('\n')
                else:
                    pair = line.split('\t')
                    # Of form \tXXXXX (named entity)
                    if (len(pair) == 2):
                        # Set type of named entity
                        if (pair[1][:-1] == "PERSON"):
                            part = "PER"
                        elif (pair[1][:-1] == "ORGANIZATION"):
                            part = "ORG"
                        elif (pair[1][:-1] == "LOCATION"):
                            part = "LOC"
                        else:
                            part = "MISC"
                            
                        
                        for i, e in enumerate(pair[0].split()):
                            if (i == 0):
                                w.write(e + '\t' + "B-" + part + '\n')
                            else:
                                w.write(e + '\t' + "I-" + part + '\n')
                                
                    # Other
                    else:
                        w.write(pair[0][:-1] + '\t' + "O\n")