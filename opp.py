class Pessoa:
    def __init__(self, nome, idade, rg, cpf):
        self.nome = nome,
        self.idade = idade,
        self.rg = rg,
        self.cpf = cpf,
        print(nome,idade,rg,cpf)



class Medico:
    def __init__(self, crm):
        self.crm = crm,
        print(crm)


class Passiente(Pessoa):
    def __init__(self, nome, idade, rg, cpf, sintomas,):
        super().__init__(nome, rg, idade, cpf)
        self.sintomas = sintomas



Passiente = Passiente('coceira')
pessoas = Pessoa('jucileide')
medico = Medico('123456789')



