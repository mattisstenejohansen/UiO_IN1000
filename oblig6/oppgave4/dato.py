
class Dato:

    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag = nyDag
        self._maaned = nyMaaned
        self._aar = nyttAar

    # A)
    def lesAar(self):
        print(self._aar)
        return self._aar

    # B) 
    def visDato(self):
        print("Dato: " + str(self._dag) + "/" + str(self._maaned) + "/" + str(self._aar))
        
    # C) 
    def sjekkDato(self, dato):

        if dato == str(self._dag) + "/" + str(self._maaned) + "/" + str(self._aar):
            print(True)

    # D) (Frivillig)
    def datoFoerEtter(self, dato):
        dato = dato.split("/")
        print(dato)
        
        if dato[2] > self._dato:
            print("Ny dato er etter original dato")
        elif dato[2] < self._dato:
            print("Ny dato er før original dato")        
    

dato1 = Dato(14, 5, 2003)

dato1.sjekkDato("14/5/2003")

dato1.datoFoerEtter("13/6/2004")

