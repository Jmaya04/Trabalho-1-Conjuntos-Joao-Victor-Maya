file = open('Maya_Trabalho1_3.txt') #Abre arquivo escolhido

texto = file.readlines()

numOperacoes = int(texto[0]) #Usa o número da primeira linha como índice de repetição no loop

index = 0

def Uniao(conjunto1, conjunto2): #Função para fazer o cálculo de união

    Resultado = []

    for i in range(len(conjunto1)):

        Resultado.append(conjunto1[i])

    for i in range(len(conjunto2)):

        if conjunto2[i] not in Resultado:

            Resultado.append(conjunto2[i])

    print("União: conjunto 1 {" + ', '.join(conjunto1) + "}, " + "conjunto 2 {" + ', '.join(conjunto2) + "}. Resultado: {" + ', '.join(Resultado) + "}")
        
def Intersecao(conjunto1, conjunto2): #Função para calcular a interseção

    Resultado = []

    for i in range(len(conjunto1)):

        if conjunto1[i] in conjunto2:

            Resultado.append(conjunto1[i])

    print("Interseção: conjunto 1 {" + ', '.join(conjunto1) + "}, " + "conjunto 2 {" + ', '.join(conjunto2) + "}. Resultado: {" + ', '.join(Resultado) + "}")

def Diferenca(conjunto1, conjunto2): #Função para calcular a diferença

    Resultado = []

    for i in range(len(conjunto1)):

        if conjunto1[i] not in conjunto2:

            Resultado.append(conjunto1[i])
        
    for i in range(len(conjunto2)):

        if conjunto2[i] not in conjunto1:

            Resultado.append(conjunto2[i])
            
    print("Diferença: conjunto 1 {" + ', '.join(conjunto1) + "}, " + "conjunto 2 {" + ', '.join(conjunto2) + "}. Resultado: {" + ', '.join(Resultado) + "}")

def Cartesiano(conjunto1, conjunto2): #Função para calcular os pares ordenados

    Resultado = {(i,j) for i in conjunto1 for j in conjunto2}

    print("Cartesiano: conjunto 1 {" + ', '.join(conjunto1) + "}, " + "conjunto 2 {" + ', '.join(conjunto2) + "}. Resultado:", Resultado)

for i in range(numOperacoes):

    conjunto = texto[2 + index].split(',') #Separa os elementos como strings

    conjunto1 = []

    conjunto2 = []

    for i in conjunto: #Adiciona os elementos do conjunto 1 em uma lista

        conjunto1.append(i.strip())

    conjunto = texto[3 + index].split(',')

    for i in conjunto: #Adiciona os elementos do conjunto 2 em uma lista

        conjunto2.append(i.strip())

    #Condição para definir qual cálculo será feito para os conjuntos

    if texto[1 + index].strip() == 'U':

        Uniao(conjunto1, conjunto2)
    
    elif texto[1 + index].strip() == 'I':

        Intersecao(conjunto1, conjunto2)

    elif texto[1 + index].strip() == 'D':

        Diferenca(conjunto1, conjunto2)

    elif texto[1 + index].strip() == 'C':

        Cartesiano(conjunto1, conjunto2)
    
    index += 3