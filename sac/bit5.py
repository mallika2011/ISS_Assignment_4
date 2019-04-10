class bitmode_5(object):
    def __init__(self):
        self.n = 0
    def unsigned5(self,x):
        a = int(0)
        l = int(16)
        for i in x:
            a = a + int(i)*l
            l=l/2
        a = int(a)
        return a
    def signed5(self,x):
        if int(x[0]) == 0:
            return self.unsigned5(x)
        else:
            x = '0' + x[1:]
            return -(self.unsigned5(x))
    def onescomp5(self,x):
        if int(x[0]) == 0:
            return self.unsigned5(x)
        else:
            a = int(0)
            l = int(16)
            for i in x:
                a = a + ((int(i)+1)%2)*l
                l=l/2
            a = int(a)
            return -a
    def twoscomp5(self,x):
        if int(x[0]) == 0:
            return self.unsigned5(x)
        else:
            a = int(0)
            l = int(16)
            for i in x:
                a = a + ((int(i)+1)%2)*l
                l=l/2
            a = int(a)
            return -(a+1)
    def binary5(self,x,y):
        n = self.unsigned5(x) + self.unsigned5(y)
        ans = bin(n)[2:]
        return ans