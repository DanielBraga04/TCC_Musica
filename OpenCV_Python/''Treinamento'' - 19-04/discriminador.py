from ram import RAM
class Driscriminador:

    def __init__(self):
        self.rams = []

    def adicionar_ram(self, ram):
        self.rams.append(ram)

    def incrementar(self, enderecos):

        for i, endereco in enumerate(enderecos):
            #Verifica se o endereço endereco está dentro dos limites da RAM correspondente
            # (self.rams[i]). len(self.rams[i].bits) retorna o número total de endereços disponíveis na RAM i.
            if endereco >= len(self.rams[i].bits):
                print(f"Endereço {endereco} fora do alcance da RAM {i+1}.")
                continue
            #Incrementando o valor no endereço endereco dentro da RAM i. self.rams[i].bits acessa o vetor
            # de bits da RAM i, e endereco é o índice desse vetor onde queremos realizar o incremento.
            self.rams[i].bits[endereco] += 1

    def criar_e_adicionar_rams(self, total_bits, nBits):
        for i in range(total_bits):
            ram = RAM(indice=i + 1, nbits=nBits)
            self.adicionar_ram(ram)

    def imprimir_rams(self):
        for ram in self.rams:
            print("RAM: ", ram.indice)
            print("Array de Bits: ", ram.bits)
            print()

    def calcular_similaridade(self, discriminador2):
        total_rams = len(self.rams)
        total_iguais = 0

        for ram1, ram2 in zip(self.rams, discriminador2.rams):
            if ram1.bits == ram2.bits:
                total_iguais += 1

        similaridade = (total_iguais / total_rams) * 100
        return similaridade

