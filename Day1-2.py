#! /usr/bin/python

total = 0

with open('/home/EH/Documents/Advent2022/Day1/input.txt') as infile:
    with open('output2.txt', 'w') as outfile:

        for line in infile:
            try:
                num = int(line)
                total += num
              
            except ValueError:
                print(total, file=outfile)
                total = 0

f = open("/home/EH/Documents/Advent2022/Day1/output2.txt", "r+")
numbers = sorted(list(map(int, f.readlines())), reverse=True)
print(numbers[:3])
h = sum(numbers[:3])
print(h)
