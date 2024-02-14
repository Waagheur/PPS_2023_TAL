import sys
import os
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

if (len(sys.argv) < 3):
    print("Not enough parameters, should be : nltkPosTagging.py source output")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                
                tokens = word_tokenize(line)

                tags = nltk.pos_tag(tokens)
                for tag in tags:
                    w.write(tag[0] + "\t" + tag[1] + "\n")
            
                w.write("\n")