diner_inv = ['Lucas','Munzer','Breaden']

for i in diner_inv:
    print (f'hey {i} would you like to go to dinner')

diner_inv[2] = "willy billy"
for i in diner_inv:
    print (f'hey {i} would you like to go to dinner')

q1 = input('hey I found biger table you want to invite anyone at the ,beginning? ')
diner_inv.insert(0, q1)
q1 = input('hey I found biger table you want to invite anyone at the ,middel? ')
diner_inv.insert(2, q1)
q1 = input('hey I found biger table you want to invite anyone at the ,end? ')
diner_inv.append(q1)
print (diner_inv)
print ('there only two spcae')
diner_inv.pop(-1)
print (diner_inv)
x = len(diner_inv)
print (f'There {i} invite')