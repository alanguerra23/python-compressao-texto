class Programa:
    def __init__(self):
        self.dicionario = {chr(i): i for i in range(256)}
        self.codigo = 256

    def fechar_programa(self):
        print('=' * 50)
        print('Programa finalizado com sucesso!')
        print('=' * 50)
        print('Criado por: Alan Silva, ED Carlos, Kennedy')
        exit()

    def start(self):
        print('=' * 50)
        print('Bem-vindo ao LZ78!')
        print('=' * 50)
        print('1 - Comprimir')
        print('2 - Descomprimir')
        print('3 - Sair')
        print('=' * 50)

        opcao = input('Digite a opção desejada: ')

        print('=' * 50)

        if opcao == '1':
            self.opcao_comprimir()

        elif opcao == '2':
            self.opcao_descomprimir()

        elif opcao == '3':
            self.fechar_programa()

        else:
            print('Opção Inválida!')
            self.fechar_programa()

    def opcao_comprimir(self):
        texto_original = input('Digite o Texto Qualquer: ')

        texto_comprimido = self.comprimir(texto_original)

        print('Texto Comprimido: ', texto_comprimido)
        print('=' * 50)

    def opcao_descomprimir(self):
        texto_original = input('Digite o Texto Qualquer: ')

        texto_comprimido = self.comprimir(texto_original)

        text_decompressao = self.descomprimir(texto_comprimido)

        print('Texto Descomprimido: ', text_decompressao)
        print('=' * 50)
        print('Texto Comprimido: ', texto_comprimido)

    def comprimir(self, original):
        if not original:
            return []

        compressao = []
        buffer = ""

        for symbol in original:
            current = buffer + symbol
            if current in self.dicionario:
                buffer = current
            else:
                compressao.append(self.dicionario[buffer])
                self.dicionario[current] = self.codigo
                self.codigo += 1
                buffer = symbol

        if buffer:
            compressao.append(self.dicionario[buffer])

        return compressao
    
    def descomprimir(self, comprimido):
        if not comprimido:
            return ""

        decompressao = ""
        dicionario = {i: chr(i) for i in range(256)}
        codigo = 256
        antigo = comprimido.pop(0)
        decompressao += dicionario[antigo]

        for new in comprimido:
            if new in dicionario:
                string = dicionario[new]
            elif new == codigo:
                string = dicionario[antigo] + dicionario[antigo][0]
            else:
                raise ValueError("Descompressão Falhou: %s" % new)

            decompressao += string
            dicionario[codigo] = dicionario[antigo] + string[0]
            codigo += 1
            antigo = new

        return decompressao


lz = Programa()

lz.start()
