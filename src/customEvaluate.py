import sys
import os

if (len(sys.argv) < 3):
    print("Not enough parameters, should be customEvaluate.py reference comparison")
    
else:
    with open(sys.argv[1], "r") as f:
        with open(sys.argv[2], "r") as w:
            trueTrue = 0
            falseTrue = 0
            falseFalse = 0
            
            # Run till we reach the end of the files
            running = True
            while (running == True):
                linesA = []
                linesB = []
            
                inLineA = True
                while (inLineA == True):
                    line = f.readline()
                    # EOF
                    if (line == ""):
                        inLineA = False
                        running = False
                    # End of sentence
                    elif (line == "\t\t\n"  # ne_reference.txt.conll
                            or line == "\n"):   # others
                        inLineA = False
                    # Regular line
                    else:
                        linesA.append(line)
                        
                inLineB = True
                while (inLineB == True):
                    line = w.readline()
                    # EOF
                    if (line == ""):
                        inLineB = False
                        running = False
                    # End of sentence
                    elif (line == "\t\t\n"  # ne_reference.txt.conll
                            or line == "\n"):   # others
                        inLineB = False
                    # Regular line
                    else:
                        linesB.append(line)
                    

                for pair in list(zip(linesA, linesB)):
                    # print(pair)
                
                    A = pair[0].split('\n')[0].split('\t')
                    B = pair[1].split('\n')[0].split('\t')
                    
                    # Skip for composed words or phrase delimitation
                    if (A[0] == ""):
                        # Phrase delimitation
                        if (B[0] == ""):
                            pass
                        else:
                            falseTrue += 1
                    else:
                        if (A[0] == B[0]):
                            if (A[1] == B[1]):
                                trueTrue += 1
                            else:
                                falseTrue += 1
                                falseFalse += 1
                        else:
                            falseTrue += 1
                            falseFalse += 1
                        
                    
                
    print("Precision : " + str(trueTrue/(trueTrue + falseTrue)))
    print("Rappel : " + str(trueTrue/(trueTrue + falseFalse)))