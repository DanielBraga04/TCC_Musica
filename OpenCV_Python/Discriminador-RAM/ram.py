class RAM:
    
    def __init__(self, indice, nbits):
        #Cria os atributos da RAM
        self.indice = indice
        self.nbits = nbits

        #Cria o array de bits inicializados com 0
        self.bits = [0] * 2 ** nbits