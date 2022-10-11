#s = []
#for i in range (1, 21):
#    if i % 5 == 0:
#        s.append(i)

#print(s)

#s1 = [i for i in range (1, 21) if i % 5 == 0]
#print(s1)

#s1 = [i **3 for i in range (1, 21) if i % 5 == 0]
#print(s1)

#s = []
#for i in range (1, 21):
#    for j in range (1, 51):
#        s.append((i, j))

#print(s)

#s1 = [(i, j) for i in range (1, 21) for j in range (1, 51)]
#print(s1)

#s = []
#for i in range (-10, 11):
#    if i > 0:
#        s.append(i ** 2)
#    else:
#        s.append(i ** 3)
#print(s)

#s1 = [i ** 2 if i > 0 else i **3 for i in range (-10, 11)]
#print(s1)

s = [7, 8, 8, 1, -1, -1]
set_set = {i for i in s}
print(set_set)
dictionary = {i: i ** 10 for i in s}
print(dictionary)