import sys
import os
import nltk
from nltk.tokenize import word_tokenize

if (len(sys.argv) < 3):
    print("Not enough parameters, should be nltkNE.py source output")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            lines = "";
            for line in f.readlines():
                lines += " " + line;
                
            tokens = word_tokenize(lines)

            tags = nltk.pos_tag(tokens)
        
            parsedLines = str(nltk.ne_chunk(tags, binary=False))
            
            for line in parsedLines.split('\n'):
                # At least : "  ()"
                if (len(line) > 3):
                    # Of form \t(XXXXX) (named entity)
                    if ((line[2] == '(') and (line[-1] == ')')):
                        elements = line[3:-1].split(' ')
                        for i, e in enumerate(elements[1:]):
                            if (i != 0):
                                w.write(' ')
                            w.write(e.split('/')[0])
                        w.write('\t' + elements[0] + '\n')