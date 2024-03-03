import sys
import os
import nltk
nltk.download('punkt')
from nltk import word_tokenize
from nltk.tag import StanfordPOSTagger

if (len(sys.argv) < 3):
    print("Not enough parameters, should be : stanfordPosTagging.py source output")
    
else:
    # Load stanford POS Tagger
    st = StanfordPOSTagger("../data/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger", 
                            path_to_jar="../data/stanford-postagger-full-2020-11-17/stanford-postagger.jar")
    
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                
                tokens = word_tokenize(line)

                tags = st.tag(tokens)
                for tag in tags:
                    w.write(tag[0] + "\t" + tag[1] + "\n")
            
                w.write("\n")