from claseConjunto import Conjunto
if __name__=='__main__':
    lista1=[1,2,3]
    lista2=[4,5,6]
    a=Conjunto(lista1)
    b=Conjunto(lista2)
    print('-------------ADD----------------')
    print('------------C=A+B---------------')
    c=a+b
    print(c)
    print('-------------SUB----------------')
    print('------------C=A-B---------------')
    c=a-b
    print(c)
    print('--------------EQ----------------')
    print('-------------A==B---------------')
    if(a==b):
        print('A Y B son iguales')
    else:
        print('A Y B NO son iguales')
