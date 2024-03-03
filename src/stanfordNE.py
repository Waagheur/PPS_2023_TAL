import sys
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger
from nltk.chunk import conlltags2tree



# Tag tokens with standard NLP BIO tags
def bio_tagger(ne_tagged):
        bio_tagged = []
        prev_tag = "O"
        for token, tag in ne_tagged:
            if tag == "O": #O
                bio_tagged.append((token, tag))
                prev_tag = tag
                continue
            if tag != "O" and prev_tag == "O": # Begin NE
                bio_tagged.append((token, "B-"+tag))
                prev_tag = tag
            elif prev_tag != "O" and prev_tag == tag: # Inside NE
                bio_tagged.append((token, "I-"+tag))
                prev_tag = tag
            elif prev_tag != "O" and prev_tag != tag: # Adjacent NE
                bio_tagged.append((token, "B-"+tag))
                prev_tag = tag
        return bio_tagged



# Create tree       
def stanford_tree(bio_tagged):
    tokens, ne_tags = zip(*bio_tagged)
    pos_tags = [pos for token, pos in stPos.tag(tokens)]

    conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]
    ne_tree = conlltags2tree(conlltags)
    return ne_tree



if (len(sys.argv) < 3):
    print("Not enough parameters, should be nltkNE.py source output")
    
else:
    # Load stanford NER
    st = StanfordNERTagger("../data/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz",
							"../data/stanford-ner-2020-11-17/stanford-ner.jar")
                            
    # Load stanford POS Tagger
    stPos = StanfordPOSTagger("../data/stanford-postagger-full-2020-11-17/models/english-bidirectional-distsim.tagger", 
                            path_to_jar="../data/stanford-postagger-full-2020-11-17/stanford-postagger.jar")

    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "w") as w:
            for line in f.readlines():
                tokens = word_tokenize(line)

                parsedLines = str(stanford_tree(bio_tagger(st.tag(tokens))))
                
                lines = parsedLines.split('\n')
                
                # Extend tree if single lined
                line = lines[0]
                if ((line[0] == '(') and (line[-1] == ')')):
                    line = line.replace(" ", "\n  ")
                    lines = line.split('\n')
                
                for line in lines:
                    # At least : "  ()"
                    if (len(line) > 3):
                        # Of form \t(XXXXX) (named entity)
                        if ((line[2] == '(') and (line[-1] == ')')):
                            elements = line[3:-1].split(' ')                             
                            
                            for i, e in enumerate(elements[1:]):
                                if (i == 0):
                                    w.write(e.split('/')[0])
                                else:
                                    w.write(' ' + e.split('/')[0])
                            w.write('\t' + elements[0] + '\n')
                                    
                        # Other
                        else:
                            w.write(line[2:-1].split('/')[0] + '\n')
                            
                w.write('\n')