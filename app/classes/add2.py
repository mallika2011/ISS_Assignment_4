from bit_4 import number_4bit
from bit_5 import number_5bit


bit = input("Number of bits?  ")

# bit=4

binary1 = input("Enter First Binary Number  ")

binary2 = input("Enter Second Binary Number  ")

print(binary1)
print(binary2)

print(int(binary1)+int(binary2))
print(len(str(binary1)))


#
# if int(bit) == 4:
#
#     b1 = number_4bit()
#     b1_unsigned = b1.b2d_4_unsigned(binary1)
#     b1_signed = b1.b2d_4_signed(binary1)
#     b1_ones = b1.b2d_4_ones(binary1)
#     b1_twos = b1.b2d_4_twos(binary1)
#
#     b2 = number_4bit()
#     b2_unsigned = b1.b2d_4_unsigned(binary2)
#     b2_signed = b1.b2d_4_signed(binary2)
#     b2_ones = b1.b2d_4_ones(binary2)
#     b2_twos = b1.b2d_4_twos(binary2)
#
#     list_b1 = [b1_twos, b1_ones, b1_unsigned, b1_signed]
#     list_b2 = [b2_twos, b2_ones, b2_unsigned, b2_signed]
#
#     # print(list_b1)
#     # print(list_b2)
#
#
#     a=number_4bit()
#     ans=[]
#
#     (bi,l1,l2,l3,l4)=a.bit4_add(list_b1,list_b2)
#     b = a.dec2bin(int(bi))
#     ans.append(b)
#     ans.append(l1)
#     ans.append(l2)
#     ans.append(l3)
#     ans.append(l4)
#
#     print(ans)
#
# elif int(bit)==5:
#     b1 = number_5bit()
#     b1_unsigned = b1.b2d_5_unsigned(binary1)
#     b1_signed = b1.b2d_5_signed(binary1)
#     b1_ones = b1.b2d_5_ones(binary1)
#     b1_twos = b1.b2d_5_twos(binary1)
#
#     b2 = number_5bit()
#     b2_unsigned = b1.b2d_5_unsigned(binary2)
#     b2_signed = b1.b2d_5_signed(binary2)
#     b2_ones = b1.b2d_5_ones(binary2)
#     b2_twos = b1.b2d_5_twos(binary2)
#
#     list_b1 = [b1_twos, b1_ones, b1_unsigned, b1_signed]
#     list_b2 = [b2_twos, b2_ones, b2_unsigned, b2_signed]
#
#     # print(list_b1)
#     # print(list_b2)
#
#     a = number_5bit()
#
#     ans = []
#
#     (bi, l1, l2, l3, l4) = a.bit5_add(list_b1, list_b2)
#     b=a.dec2bin(int(bi))
#
#
#     ans.append(b)
#     ans.append(l1)
#     ans.append(l2)
#     ans.append(l3)
#     ans.append(l4)
#
#     print(ans)
