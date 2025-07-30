t = []
n = int (input ("Enter number of elements:"))
print ("Enter", n, "elements")
for i in range (n):
    t.append(int(input()))
t = tuple (t)
fr = [None] * n
visited = -1
for i in range (n):
    count = 1
    for j in range (i + 1, n):
        if (t[i] == t[j]):
            count+=1
            fr[j] = visited
    if (fr[i] != visited):
        fr[i] = count
print ("-----------------------")
print ("| Element | Frequency |")
print ("-----------------------")
for i in range (n):
    if (fr[i] != visited):
        print ("|" + "     " + str(t[i]) + "   |   " + str (fr[i]) + "       |")
print ("-----------------------")
