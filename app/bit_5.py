class number_5bit:
    def __init__(self):
        self.num = 0

    def b2d_5_unsigned(self, str):
        i = 0
        decimal = 0
        j = len(str)-1

        for i in range(5):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        return (decimal)

    def b2d_5_signed(self, str):
        i = 0
        decimal = 0
        j = len(str)-1

        for i in range(4):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        if str[0] == '1':
            decimal = decimal*-1

        return (decimal)

    def b2d_5_ones(self, str):
        i = 0
        decimal = 0
        j = len(str)-1
        msb = -(pow(2, 4)-1)*int(str[0])

        for i in range(4):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        decimal = decimal+msb
        return (decimal)

    def b2d_5_twos(self, str):
       i = 0
       decimal = 0
       j = len(str)-1
       msb = -(pow(2, 4)*int(str[0]))
       for i in range(4):
           z = pow(2, i)
           decimal = decimal + z*int(str[j])
           j = j-1

       decimal = decimal+msb
       return (decimal)

    

    def dec2bin(self, val):

        b = ""
        while val > 0:
            if(val %2==0):
                b = b+'0'
            else:
                b = b+'1'
            val = int(val)/2

        b=b[::-1]
        return b

    def bit5_add(self, list_b1, list_b2):
        # ans=[]

        umax = 31
        umin = 0
        smax = 15
        smin = -15
        omax = 15
        omin = -15
        tmax = 15
        tmin = -16
        sum_twos = list_b1[0]+list_b2[0]
        # ans.append(sum_unsigned)
        sum_ones = list_b1[1]+list_b2[1]
        # ans.append(sum_signed)
        sum_unsigned = list_b1[2]+list_b2[2]
        # ans.append(sum_ones)
        sum_signed = list_b1[3]+list_b2[3]
        # ans.append(sum_twos)
        res=sum_unsigned

        if sum_unsigned > umax or sum_unsigned < umin:
            sum_unsigned = "Overflow ("+str(sum_unsigned)+")"

        if sum_signed > smax or sum_signed < smin:
            sum_signed = "Overflow ("+str(sum_signed)+")"

        if sum_ones > omax or sum_ones < omin:
            sum_ones = "Overflow ("+str(sum_ones)+")"

        if sum_twos > tmax or sum_twos < tmin:
            sum_twos = "Overflow ("+str(sum_twos)+")"

        # binary=dec2bin(sum_unsigned)

        return (res,sum_twos, sum_ones, sum_unsigned, sum_signed)


# a = number_5bit()
# unsigned = a.b2d_5_unsigned("11001")
# print(unsigned)
# signed = a.b2d_5_signed("11001")
# print(signed)
# ones = a.b2d_5_ones("11001")
# print(ones)
# twos = a.b2d_5_twos("11001")
# print(twos)
