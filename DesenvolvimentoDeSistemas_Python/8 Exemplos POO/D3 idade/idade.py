class Idade:
    def __init__(self,ano, mes, dia):
        self.ano = ano
        self.mes = mes
        self.dia = dia

        self.anoA = 2019
        self.mesA = 4
        self.diaA = 12


        self.totAnos = 0
        self.totDias = 0

    def totalAnos(self):
        self.totAnos = (2019 - self.ano) - 1
        if self.mesA >= self.mes:
            self.totAnos += 1

        return self.totAnos

    def totalDias(self):
        self.totAnos = 0
        # Conta os anos
        self.totDias = (365 * self.totalAnos())

        # Conta os meses
        i = 1
        while i < self.mesA:
            self.totDias += 31
            i += 1

        # Conta ate os dias atuais
        self.totDias += self.diaA

        # ======================Precisao======================================
        #  contagem no mes do nascimento
        dia= self.dia
        if self.mes % 2 == 0:
            while dia <= 31:
                self.totDias += 1
                dia += 1

        else:
            while dia <= 30:
                self.totDias += 1
                dia += 1

        #  contagem ate o final do ano
        mes = self.mes
        while mes < 12:
            self.totDias += 31
            mes += 1
        return self.totDias
