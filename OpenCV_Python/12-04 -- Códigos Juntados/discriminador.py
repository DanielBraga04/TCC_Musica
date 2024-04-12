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

