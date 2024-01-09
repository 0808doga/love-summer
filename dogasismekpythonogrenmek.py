c = 'c'
list = ['d','a','b','c'] 

print(list)
list.sort()
print(list)


def doga(dob):
    return 2023-dob
    

yas = doga(2005)
print(yas)


def sayi(x):
    return 2*x+2

x=sayi(10)
print(x)


def sinav(x):
    if x>50 or x==50: 
        print('gecti')
    elif x<50:  
        print('kaldi')


sinav(60)
sinav(49)
sinav(51)
sinav(50)

def sayi(x):
    return x*x/4+3  

x=sayi(2)
print(x)


def sinav(x):
    if x>80:
        print('A')
    elif x>70:
        print('B')
    elif x>60: 
        print('C')        
    else:
        print('kaldi')

sinav(67)

sayiliste = [10, 20 , 30, 40, 50]

toplam = 0
for i in range(0, len(sayiliste)):
    toplam += sayiliste[i]

print(toplam / len(sayiliste))   












