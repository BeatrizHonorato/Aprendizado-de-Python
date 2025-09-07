class Veiculos:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
    def descricao(self):
      return "Veiculos: "

class Moto(Veiculos):
    def descricao(self):
        return f"Modelo da moto: {self._modelo}, Marca: {self._marca}, Ano: {self._ano}"

class Carro(Veiculos):
    def descricao(self):
        return f"Modelo do carro: {self._modelo}, Marca: {self._marca}, Ano: {self._ano}"

class Caminhao(Veiculos):
    def descricao(self):
        return f"Modelo do caminhão: {self._modelo}, Marca: {self._marca}, Ano: {self._ano}"
    
moto1 = Moto("Honda", "S100 RR", 2026)
carro1 = Carro("Ford", "Fusion", 2016)
caminhao1 = Caminhao("Volvo", "FH", 2020)

print(f"{moto1.descricao()}")
print(f"{carro1.descricao()}")
print(f"{caminhao1.descricao()}")