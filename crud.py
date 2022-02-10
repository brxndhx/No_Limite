import random

print('Bem vindo ao \033[31mNo Limite\033[m\nO seu objetivo é chegar ao outro lado sem cair no abismo, será que você consegue?'
'\nSuas opções são ir para frente, esquerda ou direita.\nEscolha seus próximos passos com cuidado e boa sorte!\n')

esq = ['esquerda', 'esq', 'e', 'es', 'l', 'left']
dir = ['dir', 'd', 'direita', 'r', 'right']
frente = ['frente', 'f', 'fre', 'front']
opcao = int
mov = ''

def verificaErro(x):
    global mov
    while x not in esq and x not in dir and x not in frente and x != '':
        x = input('\nVi aqui que você informou uma palavra que não entendi, pode tenter novamente? ').lower().strip()
    mov = x

while opcao != 0:

    mov = input('Você está no plano 1: Qual seu movimento? ').lower().strip()
    verificaErro(mov)
    
    if mov in esq:

        mov = input('\nVocê chegou ao plano 2: Qual seu movimento? ').lower().strip()
        verificaErro(mov)
        
        if mov in esq:

            print('\033[31m\nVocê morreu afogado!!!\033[m')

        elif mov in frente:

            mov = input('\nVocê está no plano 5: Qual seu movimento? ').lower().strip()
            verificaErro(mov)

            if mov in esq:
                print('\033[31m\nVocê morreu afogado!!!\033[m')

            elif mov in frente:

                mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
                elif mov in frente or mov in dir:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in dir:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

        elif mov in dir:

            mov = input('\nVocê chegou ao plano 6: Qual seu movimento? ').lower().strip()
            verificaErro(mov)

            if mov in esq:

                mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
                elif mov in frente or mov in dir:
                    print('\nVocê caiu no abismo!!!')

            elif mov in frente:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in dir:

                mov = input('\nVocê está no plano 8: Qual seu movimento? ').lower().strip()
                verificaErro(mov)
                
                if mov in esq:

                    mov = input('\nVocê está no plano 9: Qual seu movimento? ').lower().strip()
                    verificaErro(mov)

                    if mov in esq:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')
                    elif mov in frente:
                        print('\033[34m\nPARABÉNS, VOCÊ SOBREVIVEU A PROVA!!!!\033[m')
                    elif mov in dir:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in frente:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in dir:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
    
    elif mov in frente:

        mov = input('\nVocê chegou ao plano 3: Qual seu movimeno? ').lower().strip()
        verificaErro(mov)

        if mov in esq:

            mov = input('\nVocê está no plano 5: Qual seu movimento? ').lower().strip()
            verificaErro(mov)
            
            if mov in esq:
                print('\033[31m\nVocê morreu afogado!!!\033[m')

            elif mov in frente:

                mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
                elif mov in frente or mov in dir:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in dir:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

        elif mov in frente:

            mov = input('\nVocê está no plano 6: Qual seu movimento? ').lower().strip()
            verificaErro(mov)

            if mov in esq:

                mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
                elif mov in frente or mov in dir:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in frente:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in dir:

                mov = input('\nVocê está no plano 8: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    
                    mov = input('\nVocê está no plano 9: Qual seu movimento? ').lower().strip()
                    verificaErro(mov)

                    if mov in esq:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')
                    elif mov in frente:
                        print('\033[34m\nPARABÉNS, VOCÊ SOBREVIVEU A PROVA!!!!\033[m')
                    elif mov in dir:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in frente:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in dir:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')

        elif mov in dir:

            mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
            verificaErro(mov)

            if mov in esq:
                print('\033[31m\nVocê morreu afogado!!!\033[m')
            elif mov in frente or mov in dir:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

        elif mov in dir:
            print('\033[31m\nVocê caiu no abismo!!!\033[m')
    
    elif mov in dir:

        mov = input('\nVocê está no plano 4: Qual seu movimento? ').lower().strip()
        verificaErro(mov)

        if mov in esq:

            mov = input('\nVocê está no plano 6: Qual seu movimento? ').lower().strip()
            verificaErro(mov)

            if mov in esq:

                mov = input('\nVocê está no plano 7: Qual seu movimento? ').lower().strip()
                verificaErro(mov)
                
                if mov in esq:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
                elif mov in frente or mov in dir:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in frente:
                print('\033[31m\nVocê caiu no abismo!!!\033[m')

            elif mov in dir:

                mov = input('\nVocê está no plano 8: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:

                    mov = input('\nVocê está no plano 9: Qual seu movimento? ').lower().strip()
                    verificaErro(mov)

                    if mov in esq:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')
                    elif mov in frente:
                        print('\033[34m\nPARABÉNS, VOCÊ SOBREVIVEU A PROVA!!!!\033[m')
                    elif mov in dir:
                        print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in frente:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

                elif mov in dir:
                    print('\033[31m\nVocê morreu afogado!!!\033[m')
        
        elif mov in frente:
            print('\033[31m\nVocê caiu no abismo!!!\033[m')
        
        elif mov in dir:

            ponte=input('\nVocê chegou na ponte: Qual seu movimento? ')

            if ponte in frente or ponte in dir:
                print('\033[31m\nVocê morreu afogado!!!\033[m')

            elif ponte in esq:

                mov = input('\nVocê está no plano 9: Qual seu movimento? ').lower().strip()
                verificaErro(mov)

                if mov in esq:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')
                elif mov in frente:
                    print('\033[34m\nPARABÉNS, VOCÊ SOBREVIVEU A PROVA!!!!\033[m')
                elif mov in dir:
                    print('\033[31m\nVocê caiu no abismo!!!\033[m')

    opcao = int(input('\nDeseja jogar novamente? Informe qualquer número para continuar e 0 para sair '))

print("\033[34m\nObrigado por jogar!\033[m")
