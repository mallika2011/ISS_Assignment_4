import printbits
def ninput():
    print("Bit Number mode(Enter 4 or 5): ")
    n = input()
    if n!='4' and n!='5':
        print("Error! Please enter 4 or 5")
        n = ninput()
    return n


n = ninput()
print("Enter first number: ")
a = input()
printbits.bitprint(a,n)
print("Enter second number: ")
b = input()
printbits.bitprint(b,n)
printbits.addprint(a,b,n)