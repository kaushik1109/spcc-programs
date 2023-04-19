mntc = 1
mdtc = 1
ala_counter = 1
ala_set = set()
ala = {}
mnt = []
mdt = {}
mystring = ''
file = open('macro.txt')
list_program = list(file)
file.close()
file = open('macro.txt', 'r+')
program = file.read()
words = program.split()
for i in range(len(words)):
    if words[i] == "MACRO":
        index = i
        # ALA
        for i in range(index + 1, len(words)):
            if words[i].startswith("&") and words[i] not in ala_set:
                ala_set.add(words[i])
                ala[ala_counter] = words[i]
                ala_counter+=1
                
for i in range(len(list_program)):
    if list_program[i] == "MACRO\n":
        mnt.append(mntc)
        line_split = list_program[i+1].split()
        mnt.append(line_split[1])
        mnt.append(mdtc)
        mntc+=1
        macro_define_index = i + 2
        mdt[mdtc] = list_program[i+1]
        mdtc+=1
        for j in range(macro_define_index, len(list_program)):
            line_split = list_program[j].split()
            for k in range(len(line_split)):
                if line_split[k] in ala_set:
                    for index in range(1, len(ala_set)+1):
                          value = ala.get(index)
                          if value == line_split[k]:
                              temp = index
                              break
                    line_split[k] = '#' + str(temp)
            mdt[mdtc] = line_split
            mdtc+=1
            
print("ALA\nIndex\tArgument")
for i in range(1, len(ala)+1):
    print(i, "\t", ala.get(i))
    
print("\n\nMNT\nIndex\tMacro Name  MDT Index")
for i in range (len(mnt)):
    print(mnt[i],"\t   ", end="")
    
print("\n\nMDT\nIndex\tCard")
for i in range (1, len(mdt)+1):
    print(i,"\t", mdt.get(i))