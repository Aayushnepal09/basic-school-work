class Arithmetic:

    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

    def mul(self,x,y):
        return x*y

    def div(self,x,y):
        if y==0:
            raise ValueError('cannot be divided by 0')
        return x/y
