a = 10
b = 20
fh = open ("D:\\KLE\\test.txt", "w")
print ("Hello World!", "From SSCE", "Sum: %d" %(a + b), sep = '\n', file = fh, flush = True)
fh.close
print ("Done")
