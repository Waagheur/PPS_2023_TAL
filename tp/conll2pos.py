import sys
import os

if (len(sys.argv) < 3):
    print("Not enough parameters, should be : conll2pos.py source output")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                if (line == "\n"):
                    w.write("\n")
                
                else:
                    l = line.split('\t')
                
                    if (l[0] != '0'):
                        w.write(l[1])
                        
                        w.write('\t')
                        
                        w.write(l[4])
                        
                        w.write('\n')