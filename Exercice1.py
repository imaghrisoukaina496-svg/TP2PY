class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire 
        self.__solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide")
    
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants ou montant invalide.")
        
    
    @property
    def solde(self):
        return self.__solde
    
    def __str__(self):
        return f"Ttulaire : {self._titulaire}, Solde : {self.solde}"
    

if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    compte.solde = 500

        