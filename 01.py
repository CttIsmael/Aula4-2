def caracter(nome,ec):
    qtd = len(nome)
    if ec.upper() == 'C':
        conj = str(input())
        qnt = len(nome + conj)
    return qtd

def main():
    nm = str(input())
    ec = str(input())
    
    
    letras = caracter(nm, ec)
    print(letras)

    
if __name__=='__main__':
    main()
