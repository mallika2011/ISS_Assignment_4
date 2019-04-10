class bitmode_4(object):
    def __init__(self):
        self.n=0
    def unsigned4(self,x):
        a = int(0)
        l = int(8)
        for i in x:
            a = a + int(i)*l
            l=l/2
        a = int(a)
        return a
    def signed4(self,x):
        if int(x[0]) == 0:
            return self.unsigned4(x)
        else:
            x = '0' + x[1:]
            return -(self.unsigned4(x))
    def binary4(self,x,y):
        n = self.unsigned4(x) + self.unsigned4(y)
        ans = bin(n)[2:]
        return ans
    def onescomp4(self,x):
        if int(x[0]) == 0:
            return self.unsigned4(x)
        else:
            a = int(0)
            l = int(8)
            for i in x:
                a = a + ((int(i)+1)%2)*l
                l=l/2
            a = int(a)
            return -a
    def twoscomp4(self,x):
        if int(x[0]) == 0:
            return self.unsigned4(x)
        else:
            a = int(0)
            l = int(8)
            for i in x:
                a = a + ((int(i)+1)%2)*l
                l=l/2
            a = int(a)
            return -(a+1)
