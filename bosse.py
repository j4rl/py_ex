import random
throws=4
addict=0

vdo=1
while vdo <= throws:
    dice=random.randrange(6)+1
    print(dice)
    #addict += dice
    vdo+=1

print(addict)
print(addict/throws)