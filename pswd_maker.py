import random
def passwordmaker():
    string1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[];:/.,<>?\\{}[]\'\"|`~"
    password=""
    for i in range(0,16):
        password+=string1[random.randint(0,len(string1)-1)]
    #print(password)
    return password
#passwordmaker()
