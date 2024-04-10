import random

def chiffrement(message):
    dictio = {}
    mess_chiffr=""
    tx = message
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|'\";:,<.>/?£¤"
    symbole = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|'\";:,<.>/?£¤")
    random.shuffle(symbole)
    cle = "".join(symbole)
    for i in carac:
        r = carac.index(i)
        dictio[i] = f"{symbole[r]}"
    for i in message:
        mess_chiffr += dictio[i]
    tp = cle
    car = ""
    ordre = ""
    liste_princ = []
    for i in cle:
        car += i
        if len(car) == 5:
            liste_princ.append(car)
            car = ""
    liste_div = liste_princ.copy()
    random.shuffle(liste_div)
    for i in liste_princ:
        for u in liste_div:
            if i == u:
                b = str(liste_div.index(u))
                if len(b) < 2:
                    b = "0"+b
                ordre += b
    cle = "".join(liste_div)
    cle += ordre
    return tx, cle, mess_chiffr

def dechiffrement(message_chiffre, li):
    code = li[-38:]
    li = li[:-38]
    lu = []
    a = ""
    for i in li:
        a += i
        if len(a) == 5:
            lu.append(a)
            a = ""
    liste = []
    intliste = []
    refaite = []
    rs = ""
    for i in code:
        rs += i
        if len(rs) == 2:
            liste.append(rs)
            rs=""  
    for i in liste:
        intliste.append(int(i))
    for i in intliste:
        refaite.append(lu[i])
    cle = "".join(refaite)
    dictio={}
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|'\";:,<.>/?£¤"
    message_decode=""
    for i in cle:
        r = cle.index(i)
        dictio[i] = f"{carac[r]}"
    for i in message_chiffre:
        message_decode+=dictio[i]
    return message_decode

chi = None 
dec = None  
chi = chiffrement("salut")
if chi is not None:
    print(f"message demandé à chiffrer: {chi[0]}")
    print(f"clé de chiffrement: {chi[1]}")
    print(f"message chiffré: {chi[2]}")
    dec = dechiffrement(chi[2], chi[1])
    print("\n")
    print(f"message déchiffré: {dec}")
