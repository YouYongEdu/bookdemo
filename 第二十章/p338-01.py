import copy
a=[11,22]
b=(a,)
c=[b,]
d=copy.copy(c)
c
d
a.append(33)
c
d
id(c)
id(d)
id(c[0])
id(d[0])
