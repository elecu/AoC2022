#! /usr/bin/python



total = 0
x=0

with open('/home/EH/Documents/Advent2022/Day1/input.txt') as infile:
    with open('output.txt', 'w') as outfile:

        for line in infile:
            try:
                num = int(line)
                total += num
                print(num, file=outfile)
            except ValueError:
                if total>x:
                    x=total
                    total=0
                else:
                    total=0
   
print(x)
