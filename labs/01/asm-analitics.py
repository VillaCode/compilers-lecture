import re
from os import system
fun = re.compile('0*(.*) <([\w\d.@]*)>:')
instruction = re.compile('.*\t([\w]*)')

funs = {}
inst = {}
with open("log", "r") as a_file:
    for line in a_file:
        res = fun.match(line)
        if res:
            funs[res.group(2)] = res.group(1)
        else:
            res = instruction.match(line)
            if res:
                if(res.group(1) not in inst):
                    inst[res.group(1)] = 1
                else:
                    inst[res.group(1)] += 1
    
print('Hi, this is the output of the analysis:')    
print('\tYou have {} kind of inst in this object file:'.format(len(inst)))    

for instr, count in inst.items():
    print('\t\t{}\t: Executed {} times'.format(instr,count))

print('\t You have {} funs'.format(len(funs)))

for func, addr in funs.items():
    print('\t\t{}\t: Located at {} addr'.format(func,addr))