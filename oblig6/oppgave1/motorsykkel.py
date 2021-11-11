
class Motorsykkel:

    def __init__(self, merke, regNummer, kmAvstand):

        self._merke = merke
        self._regNummer = regNummer
        self._kmAvstand = kmAvstand

    def kjor(self, km):
        self._kmAvstand += km
        

    def hentKilometerstand(self):
        print(self._kmAvstand)
        return self._kmAvstand

    def skrivUt(self):
        print("Merke: " + self._merke)
        print("Registreringsnummer: " + str(self._regNummer))
        print("Kilometerstand: " + str(self._kmAvstand))



