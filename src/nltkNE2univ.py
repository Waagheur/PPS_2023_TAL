import sys
import os

if (len(sys.argv) < 4):
    print("Not enough parameters, should be : nltkNE2univ.py source dict output")
    
else:
    with open (sys.argv[2], "r") as dic:
        ptbToUniv = {}
        for line in dic.readlines():
            if (line != '\n'):
                pair = line.split()
                ptbToUniv[pair[0]] = pair[1]
        
        with open(sys.argv[1], "r") as f:
            with open(sys.argv[3], "w") as w:
                for line in f.readlines():
                    
                    pair = line.split('\t')

                    if (len(pair) == 2):

                        w.write(pair[0])
                        w.write('\t')
                        w.write(ptbToUniv[pair[1][:-1]])
                
                    w.write("\n")