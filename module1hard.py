journal = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students))

a = len(grades[0])
a1 = sum(grades[0])
a2 = sum(grades[0])/len(grades[0])
journal['Aaron'] = a2

b = len(grades[1])
b1 = sum(grades[1])
b2 = sum(grades[1])/len(grades[1])
journal['Bilbo'] = b2

c = len(grades[2])
c1 = sum(grades[2])
c2 = sum(grades[2])/len(grades[2])
journal['Johnny'] = c2

d = len(grades[3])
d1 = sum(grades[3])
d2 = sum(grades[3])/len(grades[3])
journal['Khendrik'] = d2

e = len(grades[4])
e1 = sum(grades[4])
e2 = sum(grades[4])/len(grades[4])
journal['Steve'] = e2

print(journal)
