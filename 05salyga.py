#ar laimingas skaičius
sk = int(input('sk='))
#salyga = (sk>=5 and sk<=10) or (sk>=20 and sk<=25)
salyga = (5<= sk <=10) or (20<= sk <=25)
if salyga :
    print('laimingas')
else:
    print('Nelaimingas')