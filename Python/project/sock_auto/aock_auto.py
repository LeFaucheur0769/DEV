f = open ("/home/randall/Proxies/proxy.txt", "r")
w = open("/home/randall/proxy.txt", "a+")
for ligne in f:
    writ = ""
    ligne = ligne.replace(":", " ")
    writ = "socks5\t" + ligne
    print(ligne)
    w.write(writ)
f.close()
w.close()
