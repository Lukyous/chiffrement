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
print(chiffrement("salut"))