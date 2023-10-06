Grade = ['A','A','B',"F"]
total = 0
for i in Grade:
    if Grade[i] == 'A':
        total += 4
    elif Grade[1] == 'B':
        total += 3
    elif Grade[1] == 'C':
        total += 2
    elif Grade[1] == 'D':
        total += 1
    elif Grade == 'F':
        total += 0
print (total)