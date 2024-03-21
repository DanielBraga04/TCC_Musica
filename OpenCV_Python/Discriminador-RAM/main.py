#IMPORT AS CLASSES PARA A MAIN
from ram import RAM
from discriminador import Driscriminador

def main():

    #CRIANDO OBJETOS DA CLASSE 'RAM'
    nBits = 3

    ram1 = RAM(1,nBits)
    ram2 = RAM(2,nBits)
    ram3 = RAM(3,nBits)
    ram4 = RAM(4,nBits)
    ram5 = RAM(5,nBits)

    #CRIANDO OBJETOS DA CLASSE 'DISCRIMINADOR'
    discri = Driscriminador()

    #CHAMANDO A FUNÇÃO PARA ADICIONAR AS RAMS EM UM ARRAY
    discri.adicionar_ram(ram1)
    discri.adicionar_ram(ram2)
    discri.adicionar_ram(ram3)
    discri.adicionar_ram(ram4)
    discri.adicionar_ram(ram5)

    endereco = [3,1,7,0,2]

    discri.incrementar(endereco)

    print()
    print("Endereço dado: ", endereco)
    print()

    print("A lista do discriminador temos: ")

    #FOR PARA IMPRIMIR O ARRAY DE RAMS DO DISCRIMINADOR
    for ram in discri.rams:
        print("RAM: ", ram.indice)
        print("Array de Bits: ", ram.bits)
        print()

    #print("Total de bits na RAM:", ram.bits)

if __name__ == "__main__":
    main()