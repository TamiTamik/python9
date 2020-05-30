owog,ner,dun = input('owog ner dun: ').split()# mozhno cherez zapyatuyu
f = open('dun.txt', 'a')
f.write('\n' + owog + ' ' + ner + ' ' + dun)#pisat' cherez '+'
f.close()