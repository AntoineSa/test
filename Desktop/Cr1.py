# -*- coding: utf-8 -*-
from tre import mini_maxi, fill_field, erase_dobles
import copy

field = raw_input("Please enter the field : ")
mini =raw_input("minimum : ")
mini = int(mini)
maxi = raw_input("maximum : ")
maxi = int(maxi)

mini, maxi = mini_maxi(mini, maxi)

a = 0
l = len(field)
list = []

field = fill_field(a,l,list,field)

print field
a = 0
b = a + 1

field, l = erase_dobles(a, b, l, field)
print field
a = 0
b = 0
dictionary = open("flist", 'w')
dictionary.truncate()

gpass = [0]
charnb = len(gpass)

def fnameA (*args):
    arg1 = args
    x = b-1
    a = 0
    gpass[x] = field[a]
    pass

while b < mini-1 :
    gpass[b] = field[a]
    gpass.append(0)
    b = b+1
    pass
charnb = len(gpass)

while charnb <= maxi :
    while a < l :
 
        gpass[b] = field[a]
        gp = copy.deepcopy(gpass)
        gp = ''.join(gp)
        dictionary.write("%s\n" % gp)
        a = a + 1
        pass

    b = b-1
    test = False
    a = field.index(gpass[b])
    a = a+1
    if a == l :
        test = True
        pass

    while test == True and b >= 0 :
        
        b = b-1
        a = field.index(gpass[b])
        a = a+1
        if a == l :
            test = True
        else :
            test = False
        pass

    if b < 0 :
        gpass.append(0)
    else :
        gpass[b] = field[a]
        pass

    a = 0
    c = b+1
    charnb = len(gpass)
    while c < charnb :
        gpass[c] = field[0]
        c = c +1
        pass
    b = charnb -1
    pass


dictionary.close()
dictionary = open ("flist", 'r')
print dictionary.read()
dictionary.close()
exit()
