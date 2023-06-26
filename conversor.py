hex ={'A' : 10,'a' : 10,'B' : 11,'b' : 11,'C' : 12,'c' : 12, 'D' : 13, 'd' : 13, 'E' : 14, 'e' : 14, 'F' : 15, 'f' : 15, 'G' : 16, 'g' : 16, 'H' : 17,
      'h' : 17, 'I' : 18,'i' : 18,'J' : 19,'j' : 19,'K' : 20,'k' : 20, 'L' : 21, 'l' : 21, 'M' : 22, 'm' : 22, 'N' : 23, 'n' : 23, 'O' : 24, 'o' : 24, 'P' : 25,
      'p' : 25,'Q' : 26,'q' : 26,'R' : 27,'r' : 27,'S' : 28,'s' : 28, 'T' : 29, 't' : 29, 'U' : 30, 'u' : 30, 'V' : 31, 'v' : 31, 'W' : 36, 'w' : 36, 'X' : 37,
      'x' : 37,'Y' : 38,'y' : 38,'Z' : 39,'z' : 39} #Dicionário para satisfazer as bases de 11 para cima.


def decimal(quantConversao, baseDeOrigem=10, baseDeDestino=10):
    saida = 0
    # Inverte-se o vetor para que seja realizado o cálculo de acordo com o index e o valor de cada número.
    back = list(quantConversao)[::-1]
    # Loop para que seja vasculhado o index na intenção de ser o expoente de cálculo(index) e o número(variavel) que será calculado e também de alterar eles de str para int.
    for index, variavel in enumerate(back):
        if baseDeOrigem <= 10:
            numDig = int(variavel)
            saida += numDig * (baseDeOrigem ** index)
        # Nas bases acima de 11 a mudança principal vem ao pensar que sejam caracteres ao invés de números inteiros, então transforma-se 
        # os números(variavel) a partir do dicionário.
        elif baseDeOrigem >= 11 and baseDeOrigem <= 40:
            if variavel in hex:
                numDig = hex[variavel]
                saida += numDig * (baseDeOrigem ** index)
            elif variavel.isdigit():
                numDig = int(variavel)
                saida += numDig * (baseDeOrigem ** index)
    # Como padrão a transformação ocorre para decimal e tem-se uma verificação para cada de destino, mas a base âncora é a base decimal.
    if baseDeDestino == 10:          
        return "Resultado = {0} na base {1}".format(saida,baseDeDestino)
        
    else:
        saidaNDecimal = ""
        # E em caso de saída não decimal ocorre as divisões sucessivas com a base de destino em busca do resto da divisão 
        while saida > 0:
            numDig = saida % baseDeDestino
            if numDig >= 10:
                saidaNDecimal = hex[numDig] + saidaNDecimal
            else:
                saidaNDecimal = str(numDig) + saidaNDecimal
            saida //= baseDeDestino
        
        return "\nResultado = {0} na base {1}".format(saidaNDecimal,baseDeDestino)
                    


numConversao = input("Insira o numero a ser convertido: ")
baseOrigem = int(input("Insira a base de origem: ") or '10')
baseDestino = int(input("Insira qual a base que você quer de saída: ") or '10')

print(decimal(numConversao, baseOrigem, baseDestino))