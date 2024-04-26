from ram import RAM
class Discriminador:

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

    def incluir_endereco(self, endereco):
        for i, end in enumerate(endereco):
            if i < len(self.rams):
                self.rams[i].bits[end] += 1
            else:
                print(f"Aviso: Endereço {end} não pôde ser incluído, RAM correspondente não encontrada.")

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

    def quantidade_rams_criadas(self):
        return len(self.rams)

    def calcular_similaridade_2(self, discri_sol, discri_fa):
        total_rams = len(self.rams)
        rams_similares_sol = 0
        rams_similares_fa = 0

        for i in range(total_rams):
            ram_trei = self.rams[i].bits
            ram_sol = discri_sol.rams[i].bits
            ram_fa = discri_fa.rams[i].bits

            for j in range(len(ram_trei)):
                if ram_trei[j] == ram_sol[j]:
                    rams_similares_sol += 1
                if ram_trei[j] == ram_fa[j]:
                    rams_similares_fa += 1

        similaridade_sol = (rams_similares_sol / (total_rams * len(ram_trei)) * 100)
        similaridade_fa = (rams_similares_fa / (total_rams * len(ram_trei)) * 100)

        if similaridade_sol > similaridade_fa:
            print("Resultado da Similaridade: É Calve de SOL")
        elif similaridade_fa > similaridade_sol:
            print("Resultado da Similaridade: É Calve de FÁ")
        else:
            print("Indeterminado!")

        print(f"SIMI SOL: {similaridade_sol:.2f}%")
        print(f"SIMI FA: {similaridade_fa:.2f}%")

