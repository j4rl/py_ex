while True:
    inp=""
    inp=input("Ange ett värde: ")
    if inp!="q":
        tal=int(inp)
        if tal<0:
            print("Negativt")
        elif tal==0:
            print("Exakt noll")
        elif tal>0:
            print("Positivt")
        else:
            print("Da fuck?!")
    else:
        break
print("Tjarå.")