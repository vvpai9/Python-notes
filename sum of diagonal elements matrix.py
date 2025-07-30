mat = []
print ("Enter 9 integers:")
for i in range (3):
    mat.append ([])
    for j in range (3):
        mat[i].append (int (input ()))
smp = sms = 0
print ("Entered 3 x 3 matrix:")
for i in range (3):
    print ("")
    for j in range (3):
        print (mat[i][j], end = " ")
for i in range (3):
    smp = smp + mat[i][i]
    sms = sms + mat[i][2 - i]
print ("")
print ("Sum of principal diagonal elements:", smp)
print ("Sum of secondary diagonal elements:", sms)
