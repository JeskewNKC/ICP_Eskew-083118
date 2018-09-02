fileName= ('source.txt')
infile= open(fileName,'r')
line = infile.readline()
while line !="":
    word_list = []
    line = line.strip('\n')
    for i in line.split('\n'):
        y =i.replace(' ','')
        chr_count = len(y)
        word_list.append(i)
        content = [len(line.split()) for line in word_list]
        print(i, *content,',',chr_count)
    line = infile.readline()
