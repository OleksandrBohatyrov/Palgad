def Lisa_andmed(i:list,p:list):
    """Inimese ja tema palga lisamine nimekirja
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list
    """

    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def Kustutamine(i:list,p:list):
    """Inimese ja tema palga eemaldamine nimekirjast
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list 
    """

    nimi=(input("Sisesta nimi "))
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
        return i,p


def Suurim_palk(i:list,p:list):
    """Maksimaalse palga leidmine
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    # ise kirjutada, kui mitu palka
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk,nimi


def Vähem_palk(i:list,p:list):
    """Minimalsem palga leidmine
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    # ise kirjutada, kui mitu palka
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk,nimi


def Soorteerimine(i:list,p:list):
    """Sorteeri palga järgi
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    v=int(input("palk 1-kahaneb, 2-kasvab? "))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi

    return i,p

def Vordsed_palgad(i:list,p:list):
    """Sorteeri palga järgi
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid)) #[1200, 2500,750,750,1200]->[1200,700]
    for palk in dublikatid:
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1
        print(palk)
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi,"saab kätte",palk)
    return i,p

def double(i:list,p:list):
    """Found min Palg
    :param: List i: Inimeste järjend
    :param: List p: Palgade järjend
    :rtype: int, str
    """
    dublikat=[o for o in p if p.count(o)>1]
    dublikat =list(set(dublikat))
    for palk in dublikat:
        n=p.count(palk)
        k=-1
        print(palk)
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)

def nimiPalk(i:list, p:list):
    """Inimese palga leidmine nime järgi
    :param: List i: Inimeste järjend
    :param: List p: Palgade järjend
    :rtype: int, str
    """
    nimi=input("Print nimi ")
    nimiList = []
    for j in range(len(i)):
        if i[j] == nimi:
            nimiList.append(p[j])
    
    print (nimi,"palgad on",nimiList) 


def palgadFilter(i:list, p:list):
    """Kuva nimekiri inimestest (palgaga), kes saavad määratud summast rohkem/vähem.
    :param: List i: Inimeste järjend
    :param: List p: Palgade järjend
    :rtype: int, str
    """
    a=int(input("1-surem, 2-vähem "))
    palgad=int(input("print palk "))
    list = []
    if a == 1:
        for j in range(len(i)):
            if palgad<p[j]:
                list.append((i[j], p[j]))
        print(f"Rohkem kui {palgad} on {list}")
    elif a == 2:
        for j in range(len(i)):
            if palgad>p[j]:
                list.append((i[j], p[j]))
        print(f"Vähem kui {palgad} on {list}")

def tomami(i:list,p:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(min(kopia))
        print(f"{j+1} inimene - {j[ind]} saab väikse palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(max(kopia))
        print(f"{j+1} inimene - {j[ind]} saab suur palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(p)+1)

def keskmine(i:list,p:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for j in range(len(p)):
        if p[j]>=kesk:
            print(f"{p[j]} saab suurem kui keskmine palk, ta saab {p[j]}")

def tulumaks(i:list,p:list): 
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    for j in range(0,len(p)):
        if p[i]<500:
            palk=p[j]
        elif 500>=p[j]<=1200:
            palk=(p[j]-500)-(p[j]-500)*0.2
        elif 1200>p[j]>=2099:
            palk=(500-(5/9)*(p[j]-1200))-(500-(5/9)*(p[j]-1200))*0.2
        else:
            palk=p[i]*0.2
        print(f"{i[j]} on maksuvaba palk {palk}")

def sorteerimine(i:list,p:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    vali=input("Sorteeri nime (1) või palga järgi (2) ")
    while vali not in ["1","2"]:
        vali=input("Kirjuta ainult 1 või 2 ")
    if vali=="1":
        vali_2=input("A–Z või Z–A ").upper()
        while vali_2 not in ["A-Z","Z-A"]:
            vali_2=input("A–Z või Z–A ").upper()
        for p in range(0,len(i)):
            for o in range(0,len(i)):
                if i[p]==i[o] and p!=o:
                    for u in range(0,len(i)):
                        i[o]+=f"_{u+1}"
                        break
        kopia=i.copy()
        i.sort()
        y1=[]
        for j in range(0,len(i)):
            ind=kopia.index(i[j])
            y1.insert(i,p[ind])
        y=y1
        if vali_2=="Z-A":
            i.reverse()
            y.reverse()
    else:
        for p in range(0,len(i)):
            for o in range(0,len(i)):
                if y[p]<y[o]:
                    abi=y[p]
                    y[p]=y[o]
                    y[o]=abi
                    abi=i[p]
                    i[p]=i[o]
                    i[o]=abi
        vali_2=input("Kasvav või kahanev järjekord ").title()
        while vali_2 not in ["Kasvav","Kahanev"]:
            vali_2=input("Kasvav või kahanev! ").title()
        if vali_2=="Kahanev":
            i.reverse()
            p.reverse()
    return i,p 

def keskpop(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype: list, list
    """
    x1=[] 
    y1=[]
    keskmine=sum(y)/len(y)
    print(f"Keskmine palk on {keskmine}")
    for j in range(0,len(x)):
        if y[j]>keskmine:
            y1.append(y[j])
            x1.append(x[j])
    x=x1 
    y=y1
    return x,y

def tint(i:list,p:list):
    """Kirjeldus...
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    for j in range(0,len(i)):
        i[j]=p[j].title()
        p[j]=round(p[j],1) 
        p[j]=int(p[j])
    return i,p

def year(i:list,p:list):
    T=int(input("Mitu aastat? "))
    for j in range(len(p)):
        p[j]=p[j]*1.05**T
    return i,p
