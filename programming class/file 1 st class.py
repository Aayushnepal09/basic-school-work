f = (open('xyz.txt','r'))
print('Initial position',f.tell)
f.seek(6)
content=f.read()
print(content)
print(type(content))
f.close
