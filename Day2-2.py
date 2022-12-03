#! /usr/bin/python

import os
os.system('./$pwd/split_columns.sh')
dir_path = os.path.dirname(os.path.realpath(__file__))

f1 = open("%s/1.txt" %(dir_path), "r")  
f2 = open("%s/2.txt" %(dir_path), "r")  

i = 0
score = 0
A=X=1
B=Y=2
C=Z=3
total=0


for line1 in f1:
    i += 1      
    for line2 in f2:

        if eval(line2) == 1:
            if eval(line1) == 3:  
                line2 == Y
                print(line2)
                score=2
            elif eval(line1) == 2:
                line2 == X
                score=1
            else:
                line2 == Z
                score=3
        elif eval(line2) == 2:
         if eval(line1) == 3:  
                 line2 = Z
                 score=3+3
         elif eval(line1) == 2:
                line2 = Y
                score=2+3
         else:
                line2 = X
                score=1+3
        elif eval(line2) == 3:
            if eval(line1) == 3:  
                line2 = X
                score=1+6
            elif eval(line1) == 2:
                line2 = Z
                score=3+6
            else:
                line2 = Y
                score=2+6
        total+=score        
        break    


print(total)
f1.close()                                       
f2.close()    
