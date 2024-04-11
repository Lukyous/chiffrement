import random
import subprocess
import time

def chiffrement(message, default_key = None):
    dictio = {}
    mess_chiffr=""
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789é!@ $%^&*()-â=+[{]}\\|'\",:à<ù>/?êè!@#_;.£"
    if default_key is not None:
        mu = default_key
        code = default_key[-34:]
        default_key = default_key[:-34]
        lu = []
        a = ""
        for i in default_key:
            a += i
            if len(a) == 6:
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
        for i in carac:
            r = carac.index(i)
            dictio[i] = f"{cle[r]}"
        for i in message:
            mess_chiffr += dictio[i]
        return mu, mess_chiffr
    else:
        symbole = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789é!@ $%^&*()-â=+[{]}\\|'\",:à<ù>/?êè!@#_;.£")
        random.shuffle(symbole)
        cle = "".join(symbole)
        for i in carac:
            r = carac.index(i)
            dictio[i] = f"{symbole[r]}"
        for i in message:
            mess_chiffr += dictio[i]
        car = ""
        ordre = ""
        liste_princ = []
        for i in cle:
            car += i
            if len(car) == 6:
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
    code = li[-34:]
    li = li[:-34]
    lu = []
    a = ""
    for i in li:
        a += i
        if len(a) == 6:
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
    st={}
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789é!@ $%^&*()-â=+[{]}\\|'\",:à<ù>/?êè!@#_;.£"
    message_decode=""
    for i in cle:
        r = cle.index(i)
        st[i] = f"{carac[r]}"
    for i in message_chiffre:
        message_decode+=st[i]
    return message_decode

def menu():
    print("""
------------------------------------------------------------------------------------------------------------------------------     
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
    choix = int(input("Quel est votre choix? ").strip())
    if choix == 1:
        txt = input("que souhaitez-vous chiffrer? ")
        ch = input("Avous vous une clé de chiffrement prédéfinis? y/n: ").lower()
        while True:
            if ch == "y":
                tr = input("Quelle est la clé à utiliser? ")
                chi = chiffrement(txt, tr)
                break
            elif ch == "n":
                chi = chiffrement(txt)
                break
            else:
                input("Le choix est mauvais, il faut mettre y(yes) ou n(no).")
        print(f"clé de chiffrement: {chi[0]}")
        print(f"message chiffré: {chi[1]}")
        txt=""
        input("Cliquer sur entrer pour retourner au menu: ")
        subprocess.run("cls", shell=True)
        menu()
    elif choix == 2:
        txt = input("texte à déchiffrer: ")
        cle = input("Clé de déchiffrement: ")
        try:
            dec = dechiffrement(txt, cle)
        except:
            print("Clé mauvaise.")
            input("Cliquer sur entrer pour retourner au menu: ")
            subprocess.run("cls", shell=True)
            menu()
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
