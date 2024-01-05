#1
from abc import ABC, abstractmethod


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass
    @abstractmethod
    def ora_de_somn(self):
        pass


#2
class GradinitaPublica(Gradinita):

    def __init__(self):
        self.elevi = {}
        self.ghiozdan = {}
    def activitate_practica(self):
        print('Copiii invata sa deseneze.')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora 5.')

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere):
        self.elevi[nume_elev] = {nume_elev:{"varsta": varsta_elev, "an_inscriere":an_inscriere}}
        print(self.elevi[nume_elev])

    def ghiozdan_elev(self, nume_elev, nr_caiete, nr_materii_pe_zi, nr_pixuri, nr_stilouri):
        self.ghiozdan[nume_elev] = {nume_elev: {"total caiete":nr_caiete, "materii":nr_materii_pe_zi,"pixuri":nr_pixuri, "stilouri":nr_stilouri}}
        print(self.ghiozdan[nume_elev])


class GradinitaPrivata(Gradinita):

    def __init__(self,valoare_taxa=5000):
        self.elevi = {}
        self.ghiozdan = {}
        self.__valoare_taxa = valoare_taxa

    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina.')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora 5')

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere, taxa_platita):
        self.elevi[nume_elev] = {nume_elev:{"varsta": varsta_elev, "an_inscriere": an_inscriere, "taxa_platita": taxa_platita}}
        print(self.elevi[nume_elev])

    @property
    def taxa(self):
        return self.__valoare_taxa

    @taxa.getter
    def taxa(self):
        print('Getter')
        return f'{self.__valoare_taxa} lei'

    @taxa.setter
    def taxa(self, taxa_noua):
        if taxa_noua < 5000:
            print('Taxa e de 5000 lei. Trebuie achitata toata suma o data')
        elif taxa_noua > 5000:
            self.__valoare_taxa = 5000
            diferenta_taxa = taxa_noua - self.__valoare_taxa
            print('Setter')
            print(f'Taxa e de 5000 lei. Ea a fost platita cu succes. Ridicati restul de bani {diferenta_taxa} ')
        else:
            self.__valoare_taxa = taxa_noua
            print('Taxa a fost platita cu succes!')


gradinita_pu = GradinitaPublica()
gradinita_pu.activitate_practica()
gradinita_pr = GradinitaPrivata()


#4
class GradinitaPublica25(GradinitaPublica):
    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar')

gradinita_25 = GradinitaPublica25()
gradinita_25.activitate_practica()
gradinita_25.ora_de_somn()

#5
gradinita_pr.adauga_elev('Toparcianu Alice', 12, 2020, 1000)
gradinita_pu.adauga_elev('Goicea Rares', 13, 2020)
gradinita_pu.ghiozdan_elev('Goicea Rares',10, 5, 4, 2)
print(gradinita_pr.taxa)
gradinita_pr.taxa = 3000
print(gradinita_pr.taxa)
gradinita_pr.taxa = 7500
print(gradinita_pr.taxa)
gradinita_pr.taxa = 5000