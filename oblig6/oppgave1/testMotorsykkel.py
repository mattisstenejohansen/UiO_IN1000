from motorsykkel import Motorsykkel

def hovedprogram():

    sykkel1 = Motorsykkel("BMW", 123, 1000)
    sykkel2 = Motorsykkel("Yamaha", 456, 2000)
    sykkel3 = Motorsykkel("Mitsubishu", 789, 500)

    sykkel1.skrivUt()
    print(" ")
    
    sykkel2.skrivUt()
    print("")
    
    sykkel3.skrivUt()
    print("")

    sykkel3.kjor(100)
    sykkel3.hentKilometerstand()


hovedprogram()
