import Objetos
from Objetos import *
from sys import exit
import pygame

#Iniciando
pygame.init()
jogo = Jogo()
jog_1 = Jogador('BRANCO', 'Branco')
jog_1.turno = True
jog_2 = Jogador('PRETO', 'Preto')
rabo = []

#Abre a Tela de inicio, espera que pressione espaço e quando pressionar o jogo comeca (jogo ativo = True)
jogo.load_menu()

#O jogo rodar até alguem ganhar
while jogo.jogo_ativo:

    #Verifica se há um evento de QUIT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Enquanto não houver uma jogada (EX: jogada_feita == False)
    while not jogo.jogada_completa:

        #Vê quem é o jogador do turno atual
        if jog_1.turno:
            jog_atual = jog_1
            jog_oposto = jog_2
        else:
            jog_atual = jog_2
            jog_oposto = jog_1

        #Remapeia o tabuleiro
        Jogo.mapa_pecas = Objetos.mapear_tabuleiro(jog_atual.pecas, jog_oposto.pecas)

        # Update nos sprites (Cria a tela e desenha os sprites que tem a desenhar) -> mesa, tabuleiro, peças de ambos os jogadores
        jogo.sprites_atuais = [(jogo.mesa_supr, jogo.mesa_rect), (jogo.tabuleiro_supr, jogo.tabuleiro_rect)]
        if jog_atual.pos_ultima_peca > -1:
            jogo.sprites_atuais.extend([jog_atual.stack_ultima_peca[jog_atual.pos_ultima_peca]])
        if jog_oposto.pos_ultima_peca > -1:
            jogo.sprites_atuais.extend([jog_oposto.stack_ultima_peca[jog_oposto.pos_ultima_peca]])
        jogo.sprites_atuais.extend(jog_atual.pecas)
        jogo.sprites_atuais.extend(jog_oposto.pecas)
        jogo.update_sprites(jogo.sprites_atuais)

        #Verifica se houve um clique no ecrã
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:

            #Se houver um clique válido para selecionar uma peça (mouse_position colide com a peça do jogador atual) a peça clicada é selecionada
                mouse_pos = pygame.mouse.get_pos()
                jog_atual.validacao_E_selecao_peca(mouse_pos)

            # Se houver algum na lista de espera e houver já uma peça no stack, o pião que tinha entrado em espera passa a ser a peça selecionada (pq o reviver utiliza a peça selecionada)
            if jog_atual.esperando >= 1:
                if jog_atual.pos_ultima_peca > -1:
                    jog_atual.peca_selecionada = jog_atual.remover_da_espera()
                    jog_atual.reviver()
                    jog_atual.esperando -= 1
        #Se houver uma peça selecionda espera por um segundo clique válido clique válido (Se é num espaço andavel, num inimigo ou peça do jogador atual)
        if jog_atual.peca_selecionada != None:
            #Fica a rodar nesse loop até a jogada tenha sido completa
            while jogo.jogada_completa == False:

                jogo.sprites_atuais = [(jogo.mesa_supr, jogo.mesa_rect), (jogo.tabuleiro_supr, jogo.tabuleiro_rect)]
                jog_atual.quadrado_verde[0][1] = jog_atual.peca_selecionada[1]
                jogo.sprites_atuais.extend(jog_atual.quadrado_verde)
                jogo.sprites_atuais.extend(jog_1.pecas)
                jogo.sprites_atuais.extend(jog_2.pecas)
                if jog_atual.pos_ultima_peca > -1:
                    jogo.sprites_atuais.extend([jog_atual.stack_ultima_peca[jog_atual.pos_ultima_peca]])
                if jog_oposto.pos_ultima_peca > -1:
                    jogo.sprites_atuais.extend([jog_oposto.stack_ultima_peca[jog_oposto.pos_ultima_peca]])
                Jogo.mapa_pecas = Objetos.mapear_tabuleiro(jog_atual.pecas, jog_oposto.pecas)
                jogo.update_sprites(jogo.sprites_atuais)



                for evento2 in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if evento2.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if evento2.type == pygame.MOUSEBUTTONDOWN:
                        if jog_atual.validacao_E_selecao_peca(mouse_pos) == False: #Caso não troque a peça selecionada é porque ali não estava nenhuma peça minha
                            if jog_atual.consegue_mover(mouse_pos): #Se a peça conseguir alcançar esse quadrado
                                quadrado = jogo.get_quadrado(mouse_pos)
                                if jog_atual.existe_inimigo(quadrado):
                                    #removo o enimigo do conjunto de pecas do jogador oposto
                                    pos_peca = 0
                                    for peca in jog_oposto.pecas:
                                        if peca[1] == quadrado:
                                            # Caso não seja um pião a ser eliminado, coloco o sprite dele fora do jogo para a mesa (uso um stack e mostro sempre o ultimo)
                                            if jog_oposto.not_piao(quadrado):
                                                jog_oposto.mover_para_stack(peca[0], peca[1])
                                            del (jog_oposto.pecas[pos_peca])
                                        pos_peca += 1
                                jog_atual.mover_peca(jog_atual.peca_selecionada[1], quadrado)

                                # Se for um pião e tiver chegado ao revive, caso não haja nenhum para reviver põe em lista de espera
                                if not jog_atual.not_piao(jog_atual.peca_selecionada[1]):
                                    if (jog_atual.cor == 'BRANCO' and jog_atual.peca_selecionada[1].x == 626) or (jog_atual.cor == 'PRETO' and jog_atual.peca_selecionada[1].x == 101):
                                        if jog_atual.pos_ultima_peca > -1:
                                            jog_atual.reviver()
                                        else:
                                            jog_atual.esperando += 1
                                            jog_atual.adicionar_na_espera((jog_atual.peca_selecionada[0], jog_atual.peca_selecionada[1]))


                                # jogada_completa passa para True
                                jogo.jogada_completa = True

                                # Peca selecionada reseta para None
                                jog_atual.peca_selecionada = None






#APOS A JOGADA SER FEITA

    #Verifica se há algum jogador que não tenha o rei vivo e se um não tiver, o jogo_ativo passa para False, Se ambos tiverem, a jogada completa passa para False e continuam a jogar
    if jog_atual.existe_rei() and jog_oposto.existe_rei():
        jogo.jogada_completa = False
        # Muda o turno do jogador
        if jog_atual == jog_1:
            jog_1.turno = False
            jog_2.turno = True
        else:
            jog_1.turno = True
            jog_2.turno = False
    else:
        jogo.jogo_ativo = False
        jogo.tela_vencedor = True

#Mostrar tela com o vencedor e esperar para clicar espaço (verifica evento)
tela = pygame.display.set_mode((800, 600))
while jogo.tela_vencedor == True:
    jog_atual.load_tela_vencedor(tela)
    for evento3 in pygame.event.get():
        #jogo.load_tela_vencedor()
        if evento3.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento3.type == pygame.KEYDOWN:
            if evento3.key == pygame.K_SPACE:
                pygame.quit()
                exit()


"""
Erros:
- Se o pião chegar ao fim e não houver nenhum para reviver, ele não revive e não fica em "lista de espera" 
"""