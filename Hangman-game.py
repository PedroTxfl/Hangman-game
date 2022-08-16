from ast import Break
import random as rand


escolha='Você entrou no código do jogo da forca!'

while escolha != '#sair':
    print('---JOGO DA FORCA---')
   
    bau=['casa', 'bolo', 'sagacidade', 'motor', 'controle', 'massa', 'teclado', 'ossos', 'lagartixa', 'computador', 'carro', 'hardware', 'garrafa', 'pedal', 'letras', 'pandemia', 'academia', 'versatilidade']
    exibir=[]
    erros=dict()

    def sortearPalavra():
        w=rand.choice(bau)
        return w
    
    word=sortearPalavra()

    bauletras=[]
    for i in word:
        bauletras.append(i)
        

    def sortearLetra():
        l=rand.choice(bauletras)
        return l

    letter=sortearLetra()

    for i in word:

        if len(bauletras)>=8:
            if letter==i:
                exibir.append(i)
            else:
                exibir.append('_')

        else:
            exibir.append('_')

       
    print(exibir)
    print(' ')


    def validarLetra():
        letra = input('Digite uma letra: ').lower()

        if word.lower().count(letra)== 0:            
            print(f'Letra "{letra}" não existe na palavra')
            erros[letra] = 1
            
        contaletras = 0
        for i in word:
            if letra == i:
                exibir[contaletras] = letra
            contaletras += 1
       
    
    while escolha != '#sair':

        validarLetra()

        print(exibir)
        print(erros)
        print(' ')

        if len(erros)==1:
            print('''+---+
|   O
|  
|    
+=======   ''')

        elif len(erros)==2:  
            print('''+---+
|   O
|   |
|    
+=======   ''')
        elif len(erros)==3:
            print('''+---+
|   O
|  /|
|    
+=======   ''')
        elif len(erros)==4:
            print('''+---+
|   O
|  /|\ 
|    
+=======   ''')
        elif len(erros)==5:
            print('''+---+
|   O
|  /|\ 
|  /
+=======   ''')

        elif len(erros)==6:

            print('''+---+
|   O
|  /|\ 
|  / \ 
+=======   ''')
            print(' ')
            print('Não foi desta vez!!')
            escolha=input('Você deseja continuar? -Para jogar mais digite qualquer coisa | -Para sair digite: #sair: ')
            if escolha!='#sair':
                break      

       

        if exibir.count('_')==0:
            print('PARABÉNS!! Você venceu.')
            escolha=input('Você deseja continuar? -Para jogar mais digite qualquer coisa | -Para sair digite: #sair: ')
            if escolha!='#sair':
                break    
        
        print(' ')

print('Você saiu.')