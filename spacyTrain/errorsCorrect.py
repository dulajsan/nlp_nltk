
a=[u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'U-B-GUI1', u'U-I-GUI1', u'U-L-GUI1', u'O']


b=[str(t) for t in a]

lst=[]

for q in b:
    if q[0]=='U':
        lst.append(q[2:])
    else:
        lst.append(q)



