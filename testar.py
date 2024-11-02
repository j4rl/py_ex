
while True:
    print("1. Mata in personer")
    print("2. Ta bort personer")
    print("3. Registrera åsikter")
    print("4. Lista personer")
    print("5. Avsluta")
    menyval=input(": ")
    #gör en tom lista med namnet 'personer' som innehåller en dictionary på 'namn' och 'åsikter'
    personer = []

    if menyval=="1": #Gör stuff här som hör till menyval 1
        while True:
            person = input("Mata in person: ")
            if person == "":
                break
            personer.append({'namn': person, 'åsikt': ''})
        print("Personer: ", personer)
    elif menyval=="2": #Gör stuff som hör till menyval 2
        #Ta bort person

        person = input("Mata in person att ta bort: ")
        for p in personer:
            if p['namn'] == person:
                personer.remove(p)
        print("Personer: ", personer)
    elif menyval=="3": #Gör stuff som hör till menyval 3
        person = input("Mata in person att registrera åsikt för: ")
        åsikt = input("Mata in åsikt: ")

        for p in personer:
            if p['namn'] == person:
                p['åsikt'] = åsikt
                break
        print("Personer: ", personer)
    elif menyval=="4": #Gör stuff som hör till menyval 4
        #lista personer som en snygg tabell
        print("Personer:")
        print("Namn\tÅsikt")
        for p in personer:
            print(p['namn'], "\t", p['åsikt'])
        break
    elif menyval=="5":
        break
    else: #Om användaren skriver något annat än 1, 2, 3 eller 4
        print("Försök igen")
print("Personer: ", personer)
print("Programmet avslutat")
