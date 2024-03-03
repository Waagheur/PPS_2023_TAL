import sys
import os

if (len(sys.argv) < 3):
    print("Not enough parameters, should be : pos2txt.py source output")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                
                if (line != "\n"):
                    w.write(line.split('\t')[0] + " ")
                else:    
                    w.write("\n")