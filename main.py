#Transformar Numeração Romana em Inteiro.

cores_texto = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;7;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'azulclaro': '\033[1;36m',
    'cinza': '\033[1;37m'
}

cores_fundo = {
    'limpa': '\033[m',
    'pretoebranco': '\033[1;40m',
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'amarelo': '\033[1;43m',
    'azul': '\033[1;44m',
    'roxo': '\033[1;45m',
    'azulclaro': '\033[1;46m',
    'cinza': '\033[1;47m'
}

titulo = ' CONVERSÃO - ALGARISMO ROMANO | INTEIRO '

print('+', '-' * len(titulo), '+')
print('| {}{}{} |'.format(cores_fundo['pretoebranco'], titulo, cores_fundo['limpa']))
print('+', '-' * len(titulo), '+')
print()

romano = str(input('Digite os algorismos romanos: ')).strip().upper()

def romano_para_natural(romano):
    numeros = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0

    for contador, algarismo in enumerate(romano):
        atual = numeros[algarismo]

        try:
            proximo = numeros[romano[contador + 1]]
        except:
            proximo = atual
        if proximo > atual:
            resultado -= atual
        else:
            resultado += atual

    return resultado

print()
print('{}O algarismo romano {} corresponde ao número: {}{}'.format(cores_texto['azul'], romano, romano_para_natural(romano), cores_texto['limpa']))