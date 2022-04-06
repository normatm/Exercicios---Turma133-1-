
def dizer_oi(nome):
    print(f'Olá, {nome}')


def somar_2_numeros(numero1, numero2):
    return numero1 + numero2

def multiplicar_2_numeros(numero1, numero2):
    return numero1 * numero2


def dividir_2_numeros(numero1, numero2):
    try:                 # tente fazer
        return numero1 / numero2
    except ZeroDivisionError:
        return 'divisao por zero'


def calcular_area(largura, comprimento):
    if eh_numero(largura)  and eh_numero(comprimento):
        if largura > 0 and comprimento > 0:
         return largura * comprimento
        else:
         return 'um ou ambos os valores de largura e comprimento são zero ou negativos'
    else:
         return 'um ou ambos os valores de largura e comprimento são letras'


def eh_numero(candidato):
    # tenta converter o valor candidato para float (numero com parte decimal)
    # se der certo é um numero, senão é um texto (string)
    try:
        float(candidato)
    except ValueError:
        return False        # se é texto (string)
    return True             # se é numero (float)






if __name__ == '__main__':  # acionador da execução do script
    dizer_oi('Norma')

    """
    numero1 = 17
    numero2 = 90
    resultado = somar_2_numeros(numero1, numero2)
    print(f'A soma de {numero1} e {numero2} é igual a {resultado}')
    print(f'{numero1}+{numero2}={resultado}')
    """
    # Soma
    resultado = somar_2_numeros(20, 30)
    print(f'O resultado da soma é  {resultado}')

    # Multiplicação
    resultado = multiplicar_2_numeros(3, 5)
    print(f' 0 resultado da multiplicação é {resultado}')

    # Divisão
    resultado = dividir_2_numeros(8, 4)
    print(f' 0 resultado da divisão é {resultado}')

    # Area
    resultado = calcular_area(5, 9)

    if eh_numero(resultado):
        print(f'Area = {resultado} m²')
    else:
        print(f'Mensagem: {resultado}')
