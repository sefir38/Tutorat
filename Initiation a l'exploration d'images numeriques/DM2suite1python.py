#decimal to binary
def decimalToBinary(n):

    print"donnez un nombre"
    n=int(input())
    while n>1:
        n1=n//2
        autre=n%2
        autre1=n1%2
        n=n1
        print "resultat",autre
    print "resultat",autre1
    return n


n=()
valeur=10
valeur=input()
print "1.convertir decimal en binaire"


while (valeur!=0):
    
    if (valeur==1):
        decimalToBinary(n)
