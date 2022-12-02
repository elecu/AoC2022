#! /usr/bin/python

import os
os.system('./$pwd/split_columns.sh')
dir_path = os.path.dirname(os.path.realpath(__file__))


#print("the directory is in %s" % (dir_path))
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
        
        if eval(line1) == eval(line2): 
            score=3+eval(line2)
            print("Draw" , line1,"+",line2,"+ 3","=",score)                
        elif eval(line2) == 1:
            if eval(line1) == 3:
                score=6+eval(line2)
                print("I win" , line1,"+",line2,"+ 6","=",score)                
            else:

                score=0+eval(line2)
                print("I lost" , line1,"+",line2,"+ 0","=",score)                
        elif eval(line2) == 2:
            if eval(line1) == 1:
                score=6+eval(line2)
                print("I win" , line1,"+",line2,"+ 6","=",score)                
            else:
                score=0+eval(line2)
                print("I lost" , line1,"+",line2,"+ 0","=",score)                
        elif eval(line2) == 3:
            if eval(line1) == 2:
                score=6+eval(line2)
                print("I win" , line1,"+",line2,"+ 6","=",score)                
            else:
                score=0+eval(line2)
                print("I lost" , line1,"+",line2,"+ 0","=",score)                
        total+=score
        break


  
print(total)
f1.close()                                       
f2.close()    
