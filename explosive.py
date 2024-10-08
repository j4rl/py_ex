tal=int(input("Ge mig! "))
print("Talet".center(10), "Summan".center(10), "Mult".center(10))
vdo=1
while vdo<=tal:
    tal_sum=vdo+vdo
    tal_mult=vdo*vdo
    print(str(vdo).center(10), str(tal_sum).center(10), str(tal_mult).center(10) )
    vdo+=1
