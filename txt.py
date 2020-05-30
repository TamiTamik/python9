# default - 'r'
f = open('data.txt','r') # r - read
# f = open('data.txt','w') # w - write
# a - add
# x - create
# t - text
# b - binar code
txt = f.readlines()
for t in txt:
    print(t)
f.close() #vsegda zakrivat' file posle redaktirovaniya
#.readline() - chitaet po strokam
#.readable() - proveryaet vozmozhno li prochitat'