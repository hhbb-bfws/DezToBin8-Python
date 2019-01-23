def dezToBin8(dez):
    bin = ''
    nDiv = int(dez)

    if (nDiv < 256) and (nDiv >= 0) :
        nMod = 0

        for i in range(0,7):
            nMod=nDiv%2
            nDiv=nDiv//2
            bin = str(nMod) + bin
    return bin

print('Dezimal zu Binär-Konvertierung')
ende = ''
while (ende != 'e'):
    dez = input('\nBitte Zahl im Dezimalsystem (0..255) eingeben: ')
    bin = dezToBin8(dez)
    print(dez, 'lautet im Binärsystem', bin)
    ende = input('\nProgramm be(e)nden? ')
