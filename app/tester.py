# import json
# import requests

# URL = "http://localhost:5000/answer"
# no_1="1000"
# no_2="1010"
# PARAMS = {"x1":no_1,"x2":no_2}

# r = requests.get(url = URL,json = PARAMS)
# data=r.json()

# #TESTCASES-4bit
# print("#1 Test Case : 1000 1010")
# if data['res'] == "overflow (10010)" and data['un'] == "overflow (18)" and data['sign'] == -2 and data['two'] == "overflow (-14)" and data['one'] == "overflow (-12)":
# 	print('#1 Test Case Passed')
# else:
# 	print('#1 Test Case Failed')

from add import answer
#Test Case 1
testcase_1="1010"
testcase_2="0101"

print("#1 Test Case : 1010 0101")

r=answer(testcase_1,testcase_2)

if r['res'] == "1111" and r['two'] == -1 and r['one'] == +0 and r['un'] == 15 and r['sign'] == 3:
    print("Test Case 1 passed\n")
else:
    print("Test Case Failed\n")
    
#Test Case 2    
testcase_1="1011"
testcase_2="1101"

print("#2 Test Case : 1011 1101")

r=answer(testcase_1,testcase_2)

if r['res'] == "11000" and r['two'] == -8 and r['one'] == -6 and r['un'] == "Overflow (24)" and r['sign'] == "Overflow (-8)":
    print("Test Case 2 passed\n")
else:
    print("Test Case 2 Failed\n")

#Test Case 3
testcase_1="1111"
testcase_2="0000"

print("#3 Test Case : 1111 0000")

r=answer(testcase_1,testcase_2)

if r['res'] == "1111" and r['two'] == -1 and r['one'] == 0 and r['un'] == 15 and r['sign'] == -7:
    print("Test Case 3 passed\n")
else:
    print("Test Case 3 Failed\n")

#Test Case 4
testcase_1="00110"
testcase_2="01011"

print("#4 Test Case : 00110 01011")

r=answer(testcase_1,testcase_2)

if r['res'] == "10001" and r['two'] == "Overflow (17)" and r['one'] == "Overflow (17)" and r['un'] == 17 and r['sign'] == "Overflow (17)":
    print("Test Case 4 passed\n")
else:
    print("Test Case 4 Failed\n")
    
#Test Case 5
testcase_1="00100"
testcase_2="01001"

print("#5 Test Case : 00100 01001")

r=answer(testcase_1,testcase_2)

if r['res'] == "1101" and r['two'] == 13 and r['one'] == 13 and r['un'] == 13 and r['sign'] == 13:
    print("Test Case 5 passed\n")
else:
    print("Test Case 5 Failed\n")
    
