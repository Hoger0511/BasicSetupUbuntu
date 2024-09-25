telefonkatalog = [] # listeformst ["fornavn" , "etternavn" , "telefonnummer"]
fil = "telefondata.txt" 


def hent_personer_fra_fil(filnavn): 
    global telefonkatalog
    with open(filnavn, 'r') as fil: 
        for linje in fil:
            person = linje.strip().split()
            telefonkatalog.append(person)

        

    hent_personer_fra_fil(fil)


def skriv_til_fil(filnavn):
    with open(filnavn, "w") as txt_file: 
        for person in telefonkatalog:
            txt_file.write(" ".join(person) + "\n")


                
def printMeny(): 
    print("--------------------- Telefonkatalog -------------------------")
    print("| 1. Legg til ny person                                      |")
    print("| 2. Søk opp person eller telefonnummer                      |")
    print("| 3. Vis alle personer                                       |")
    print("| 4. Avslutt                                                 |")
    print("--------------------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall): 
    if valgtTall == "1": # input returnerer string, derfor "1"
        registrerPerson()
    elif valgtTall == "2":
        sokperson()
        printMeny()
    elif valgtTall == "3":
        visAllePerson()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avlustte: J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"): # Sjekker bare for ja 
            skriv_til_fil(fil) 
            exit()
    else: 
        nyttForsoek = input ("Ugyldig valg. Velg et tall mellom 1-4: ")
        utfoerMenyvalg(nyttForsoek) 

def registrerPerson(): 
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")
    nyregristrering = [fornavn , etternavn , telefonnummer]
    telefonkatalog.append(nyregristrering)

    print("{0} {1} er registrert med telefonnummer {2}"
        .format(fornavn , etternavn , telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


def visAllePerson():
    if not telefonkatalog: 
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else: 
        print("***********************************************"
                "***********************************************")
        for personer in telefonkatalog: 
            print("* Fornavn: {:15s} Etternavn: {:15s} Telfonnummmer: {:8s}"
                    .format(personer[0], personer[1], personer[2]))
        print("***********************************************"
                "***********************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
        
def sokperson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
    else: 
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-4: ")
        if sokefelt == "1": 
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2": 
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3": 
            telefonnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", telefonnummer)
        elif sokefelt == "4": 
            return
        else:
            print("Ugyldig valg. Velg et tall mellom 1-4.")
            sokperson()

def finnPerson(typesok, sokeTekst): 
    found = False
    for personer in telefonkatalog:
        if typesok == "fornavn" and personer[0] == sokeTekst:
            print("{0} {1} har telefonnummer {2}".format(personer[0], personer[1], personer[2]))
            found = True
        elif typesok == "etternavn" and personer[1] == sokeTekst:
            print("{0} {1} har telefonnummer {2}".format(personer[0], personer[1], personer[2]))
            found = True
        elif typesok == "telefonnummer" and personer[2] == sokeTekst:
            print("Telefonnummer {0} tilhører {1} {2}".format(personer[2], personer[0], personer[1]))
            found = True
    if not found:
        print("Ingen treff for søketekst: " + sokeTekst)
    return


    # typesok angir om man søker på fornavn, etternavn  eller telefonnummer
def finnPerson(typesok, sokeTekst): 
    for personer in telefonkatalog:
        if typesok == "fornavn": 
            if personer [0] == sokeTekst:
                print("{0} {1} har telefonnummer {2}"
                    .format(personer[0], personer[1], personer[2]))
                
            else: 
                print("Finner ingen personer med fornavn" + sokeTekst)
                sokperson()
        elif typesok == "etternavn":
            if personer[1] == sokeTekst:
                print("{0} {1} har telefonnummer {2}"
                    .format(personer[0], personer [1], personer[2]))
        else: 
            if personer[2] == sokeTekst:
                print("Telefonnummer {0} tilhører {1} {2}"
                      .format(personer[2], personer[0], personer[1]))
            else:
                print("Telefonnummer " + sokeTekst + " er ikke registrert. \n")


        
printMeny() # Starter programmet ved å skrive menyen første gang 





    
            
                