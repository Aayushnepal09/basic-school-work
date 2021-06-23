f=open('xyz.txt','r')           # r for read  # w for read # a for append 3 # x+ taja file
y=open('abc.txt','w')
y.write(f.read())
f.close()
y.close()