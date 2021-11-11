class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist.split(' ')


    def spill(self):   
        print("Spiller " + self._tittel + " av " + str(self._artist))

    def sjekkArtist(artistNavn):
        
        if artistNavn in self._artist:
            print(True)


sang1 = Sang("Shallow", "Lady Gaga")

sang1.spill()

sang1.sjekkArtist("Lady")

