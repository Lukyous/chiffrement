import random

def chiffrement(message):
    dictio = {}
    chiffrage = ""
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    symbole = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|;:'\",<.>/?")
    random.shuffle(symbole)
    cle = "".join(symbole)
    for i in carac:
        r = carac.index(i)
        dictio[i] = f"{symbole[r]}"
    for i in message:
        message = message.replace(i, dictio[i])
    return f"cle=\t{cle}\nchiffrement=\t{message}"

def dechiffrement(message_chiffre, cle):
    dictio={}
    carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    for i in cle:
        r = cle.index(i)
        dictio[i] = f"{carac[r]}"
    for i in message_chiffre:
        message_chiffre = message_chiffre.replace(i, dictio[i])
    return f"déchiffrement:{message_chiffre}"
    
#print(chiffrement("salut"))
dechiffrement("hL8VK", """La.A^qYyrcX8I+gF[<hKV(nH,smCj]pD!1R_ZPNk'=4x%Sit@0;6>u7vo5O2)3*bU:TWB |G}f{#eMl&$"wJQd9z?/E\-""")
