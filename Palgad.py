from module import *


palgad=[1200,2500,750,395,1700]
inimesed=["A","B","C","D","A"]

while True:
    print(inimesed)
    print(palgad)
    menu=int(input("valik:\n1-lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Vähem palk\n5-Sort\n6--\n7-Otsi palka inimese nime järgi/n8-Nimekiri inimestest (palgaga), kes saavad määratud summast rohkem/vähem\n8--"))
    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=Lisa_andmed(inimesed, palgad)
    elif menu==2:
        imimesed,palgad=Kustutamine(inimesed, palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print("Suurim palk on",palk, nimi)
    elif menu==4:
        palk,nimi=Vähem_palk(inimesed,palgad)
        print("vähem palk pn", palk, nimi)
    elif menu==5:
        inimesed,palgad=Soorteerimine(inimesed,palgad)
    elif menu==6:
         double(inimesed,palgad)
    elif menu==7:
       nimiPalk(inimesed,palgad)
    elif menu==8:
         palgadFilter(inimesed,palgad)
    elif menu==9:
        tomami(inimesed,palgad)
    elif menu==10:
        keskmine(inimesed,palgad)
    elif menu==11:
        tulumaks(inimesed,palgad)
    elif menu==12:
        sorteerimine(inimesed,palgad)
    elif menu==13:
        keskpop(inimesed,palgad)
    elif menu==14:
        tint(inimesed,palgad)
    elif menu==15:
        year(inimesed,palgad)
    elif menu==16:
        reversed
