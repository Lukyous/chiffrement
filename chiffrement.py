import random
import subprocess
import time
def chiffrement(message):
    dictio = {}
    mess_chiffr=""
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
    return cle, mess_chiffr

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

def menu():
    print("""
-----------------------------------------------------------------------------------------------------------------------------      
|     _          _                                                  _      _     ___     ___                                 |
|    | |        | |                                                | |    (_)   / __)   / __)                                |
|    | |  _   _ | |  _  _   _   ___   _   _   ___             ____ | |__   _  _| |__  _| |__   ____  _____   ____  _____     |
|    | | | | | || |_/ )| | | | / _ \ | | | | /___)           / ___)|  _ \ | |(_   __)(_   __) / ___)(____ | / _  || ___ |    |
|    | | | |_| ||  _ ( | |_| || |_| || |_| ||___ |          ( (___ | | | || |  | |     | |   | |    / ___ |( (_| || ____|    |
|     \_)|____/ |_| \_) \__  | \___/ |____/ (___/            \____)|_| |_||_|  |_|     |_|   |_|    \_____| \___ ||_____)    |
|                      (____/                                                                              (_____|           |
------------------------------------------------------------------------------------------------------------------------------  
""")
    print("\n1) Chiffrer\n2) Déchiffrer")
    choix = int(input("Quel est votre choix?").strip())
    if choix == 1:
        txt = input("que souhaitez-vous chiffrer? ")
        chi = chiffrement(txt)
        print(f"clé de chiffrement: {chi[0]}")
        print(f"message chiffré: {chi[1]}")
        txt=""
        input("Cliquer sur entrer pour retourner au menu: ")
        subprocess.run("cls", shell=True)
        menu()
    elif choix == 2:
        txt = input("test à déchiffrer: ")
        cle = input("Clé de déchiffrement: ")
        dec = dechiffrement(txt, cle)
        print("\n")
        print(f"message déchiffré: {dec}")
        input("Cliquer sur entrer pour retourner au menu: ")
        subprocess.run("cls", shell=True)
        menu()
    else:
        print("Erreur, vous pouvez choisir soit 1, soit 2.")
        u=3
        for i in range(3):
            print(u, end="", flush=True)
            time.sleep(1)
            print("\b \b", end="", flush=True)
            u -= 1
        subprocess.run("cls", shell=True)
        u=3
        menu()

menu()
