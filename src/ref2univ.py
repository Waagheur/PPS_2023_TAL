import sys
import os

if (len(sys.argv) < 5):
    print("Not enough parameters, should be ref2univ.py source dictREF2PTB dictPTB2UNIV output")
    
else:
    refToPtb = {}
    with open (sys.argv[2], "r") as dic:
        for line in dic.readlines():
            if (line != '\n'):
                pair = line.split()
                refToPtb[pair[0]] = pair[1]
       
    ptbToUniv = {}
    with open (sys.argv[3], "r") as dic:
        for line in dic.readlines():
            if (line != '\n'):
                pair = line.split()
                ptbToUniv[pair[0]] = pair[1]
                
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[4], "w") as w:
            for line in f.readlines():
            
                pair = line.split('\t')

                if (len(pair) == 2):

                    w.write(pair[0])
                    w.write('\t')
                    
                    # If tag doesn't exist in dict, just replicate
                    if ((pair[1][:-1]) in refToPtb.keys()):
                        if ((refToPtb[pair[1][:-1]]) in ptbToUniv.keys()):
                            w.write(ptbToUniv[refToPtb[pair[1][:-1]]])
                        else:
                            w.write(refToPtb[pair[1][:-1]])
                    else:
                        w.write(pair[1][:-1])
                        
                    # If "word" is composed, skips as many lines as there is spaces
                    for i in range(0, len(pair[0].split())-1):
                        w.write("\n\t")
            
                w.write("\n")