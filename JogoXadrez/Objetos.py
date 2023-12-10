import pygame
import sys
pygame.init()
class Jogo(): #Classe onde vão as mecânicas do jogo
    def __init__(self):
        self.letras_foramt = pygame.font.Font('Sprites/letras.ttf', 65)
        self.icone = pygame.image.load('Sprites/Pecas_Sprites/icone.png')
        self.tela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Chess')
        pygame.display.set_icon(self.icone)

        self.mesa_supr = pygame.image.load('Sprites/Pecas_Sprites/Mesa.png')
        self.mesa_rect = self.mesa_supr.get_rect(topleft=(0, 0))
        self.tabuleiro_supr = pygame.image.load('Sprites/Pecas_Sprites/tabuleiro.png')
        self.tabuleiro_rect = self.mesa_supr.get_rect(topleft=(100, 0))

        self.tela_menu = True
        self.jogo_ativo = False
        self.tela_vencedor = False
        self.jogada_completa = False
        self.sprites_atuais = []
        self.lista_rect_tabuleiro = []
        self.criar_retangulos_tabuleiro()

    mapa_pecas = [] #mapear no começo do jogo
    lista_rect_tabuleiro = []
    def update_sprites(self, lista_sprites): #coloca na tela os sprites dentro de uma lista com supr e rect
        if len(lista_sprites) > 0:
            pos = 0
            for sprite in lista_sprites:
                pos += 1
                self.tela.blit(sprite[0], sprite[1])
            pygame.display.update()
    def load_menu(self): #Carrega o menu

        #menu
        self.menu_supr = pygame.image.load('Sprites/Pecas_Sprites/Mesa.png')
        self.menu_rect = self.menu_supr.get_rect(topleft=(0, 0))
        self.tab_supr = pygame.image.load('Sprites/Pecas_Sprites/tab.png')
        self.tab_rect = self.tab_supr.get_rect(center=(400, 250))

        #texto
        self.txt1_supr = self.letras_foramt.render("Pressione  Espaco  Para  Comecar", True, ('Black'))
        self.txt1_rect = self.txt1_supr.get_rect(center=(400, 500))

        #adicionar ao sprites
        self.sprites_atuais = [(self.menu_supr, self.menu_rect), (self.txt1_supr, self.txt1_rect), (self.tab_supr, self.tab_rect)]


        #Espera que seja inserido espaço para ativar o jogo e limpar a lista de sprites
        while self.tela_menu:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        self.tela_menu = False
            self.update_sprites(self.sprites_atuais)
        self.sprites_atuais = []
        self.jogo_ativo = True
    def criar_retangulos_tabuleiro(self):

        self.quadrado_supr = pygame.image.load('Sprites/quadrado.png')

        self.quadrado1_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 75))
        self.quadrado2_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 75))
        self.quadrado3_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 75))
        self.quadrado4_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 75))
        self.quadrado5_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 75))
        self.quadrado6_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 75))
        self.quadrado7_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 75))
        self.quadrado8_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 75))
        self.quadrado9_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 150))
        self.quadrado10_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 150))
        self.quadrado11_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 150))
        self.quadrado12_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 150))
        self.quadrado13_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 150))
        self.quadrado14_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 150))
        self.quadrado15_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 150))
        self.quadrado16_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 150))
        self.quadrado17_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 225))
        self.quadrado18_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 225))
        self.quadrado19_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 225))
        self.quadrado20_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 225))
        self.quadrado21_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 225))
        self.quadrado22_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 225))
        self.quadrado23_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 225))
        self.quadrado24_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 225))
        self.quadrado25_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 300))
        self.quadrado26_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 300))
        self.quadrado27_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 300))
        self.quadrado28_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 300))
        self.quadrado29_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 300))
        self.quadrado30_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 300))
        self.quadrado31_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 300))
        self.quadrado32_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 300))
        self.quadrado33_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 375))
        self.quadrado34_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 375))
        self.quadrado35_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 375))
        self.quadrado36_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 375))
        self.quadrado37_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 375))
        self.quadrado38_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 375))
        self.quadrado39_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 375))
        self.quadrado40_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 375))
        self.quadrado41_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 450))
        self.quadrado42_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 450))
        self.quadrado43_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 450))
        self.quadrado44_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 450))
        self.quadrado45_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 450))
        self.quadrado46_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 450))
        self.quadrado47_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 450))
        self.quadrado48_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 450))
        self.quadrado49_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 525))
        self.quadrado50_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 525))
        self.quadrado51_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 525))
        self.quadrado52_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 525))
        self.quadrado53_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 525))
        self.quadrado54_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 525))
        self.quadrado55_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 525))
        self.quadrado56_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 525))
        self.quadrado57_rect = self.quadrado_supr.get_rect(midbottom=(137.5, 600))
        self.quadrado58_rect = self.quadrado_supr.get_rect(midbottom=(212.5, 600))
        self.quadrado59_rect = self.quadrado_supr.get_rect(midbottom=(287.5, 600))
        self.quadrado60_rect = self.quadrado_supr.get_rect(midbottom=(362.5, 600))
        self.quadrado61_rect = self.quadrado_supr.get_rect(midbottom=(437.5, 600))
        self.quadrado62_rect = self.quadrado_supr.get_rect(midbottom=(512.5, 600))
        self.quadrado63_rect = self.quadrado_supr.get_rect(midbottom=(587.5, 600))
        self.quadrado64_rect = self.quadrado_supr.get_rect(midbottom=(662.5, 600))

        Jogo.lista_rect_tabuleiro = [
            self.quadrado1_rect,
            self.quadrado2_rect,
            self.quadrado3_rect,
            self.quadrado4_rect,
            self.quadrado5_rect,
            self.quadrado6_rect,
            self.quadrado7_rect,
            self.quadrado8_rect,
            self.quadrado9_rect,
            self.quadrado10_rect,
            self.quadrado11_rect,
            self.quadrado12_rect,
            self.quadrado13_rect,
            self.quadrado14_rect,
            self.quadrado15_rect,
            self.quadrado16_rect,
            self.quadrado17_rect,
            self.quadrado18_rect,
            self.quadrado19_rect,
            self.quadrado20_rect,
            self.quadrado21_rect,
            self.quadrado22_rect,
            self.quadrado23_rect,
            self.quadrado24_rect,
            self.quadrado25_rect,
            self.quadrado26_rect,
            self.quadrado27_rect,
            self.quadrado28_rect,
            self.quadrado29_rect,
            self.quadrado30_rect,
            self.quadrado31_rect,
            self.quadrado32_rect,
            self.quadrado33_rect,
            self.quadrado34_rect,
            self.quadrado35_rect,
            self.quadrado36_rect,
            self.quadrado37_rect,
            self.quadrado38_rect,
            self.quadrado39_rect,
            self.quadrado40_rect,
            self.quadrado41_rect,
            self.quadrado42_rect,
            self.quadrado43_rect,
            self.quadrado44_rect,
            self.quadrado45_rect,
            self.quadrado46_rect,
            self.quadrado47_rect,
            self.quadrado48_rect,
            self.quadrado49_rect,
            self.quadrado50_rect,
            self.quadrado51_rect,
            self.quadrado52_rect,
            self.quadrado53_rect,
            self.quadrado54_rect,
            self.quadrado55_rect,
            self.quadrado56_rect,
            self.quadrado57_rect,
            self.quadrado58_rect,
            self.quadrado59_rect,
            self.quadrado60_rect,
            self.quadrado61_rect,
            self.quadrado62_rect,
            self.quadrado63_rect,
            self.quadrado64_rect,
        ]

    def get_quadrado(self, posicao_do_mouse):
        for quadrado in Jogo.lista_rect_tabuleiro:
            if quadrado.collidepoint(posicao_do_mouse):
                return quadrado

#Mapa de todos os quadrados se existe ou não peça
def mapear_tabuleiro(lista_pecas_jog1, lista_pecas_jog2):
    tabuleiro_pecas = [False] * 64
    quad = 0
    #percorrendo pelo tabuleiro
    pecas = []
    pecas.extend(lista_pecas_jog1)
    pecas.extend(lista_pecas_jog2)
    for lin in range(0, 8):
        for col in range(0, 8):
            for peca in pecas:
                if (101 + 75*col, 75*lin) == (peca[1].x, peca[1].y):
                    tabuleiro_pecas[quad] = True
            quad += 1
    return tabuleiro_pecas


class Jogador():
    def __init__(self, BRANCO_ou_PRETO, nome):
        self.cor = BRANCO_ou_PRETO
        self.nome = nome
        self.criar_pecas()
        self.turno = False
        self.peca_selecionada = None
        self.stack_ultima_peca = []
        self.pos_ultima_peca = -1
        self.quadrado_verde_supr = pygame.image.load('Sprites/quadrado_verde.png').convert()
        self.quadrado_verde = [[self.quadrado_verde_supr, None]]
        self.esperando = 0
        self.lista_espera = []

    def criar_pecas(self):
        if self.cor == 'BRANCO':
            # PIÕES
            self.piao1_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao1_rect = self.piao1_supr.get_rect(midbottom=(212.5, 75))
            self.piao2_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao2_rect = self.piao2_supr.get_rect(midbottom=(212.5, 150))
            self.piao3_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao3_rect = self.piao3_supr.get_rect(midbottom=(212.5, 225))
            self.piao4_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao4_rect = self.piao4_supr.get_rect(midbottom=(212.5, 300))
            self.piao5_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao5_rect = self.piao5_supr.get_rect(midbottom=(212.5, 375))
            self.piao6_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao6_rect = self.piao6_supr.get_rect(midbottom=(212.5, 450))
            self.piao7_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao7_rect = self.piao7_supr.get_rect(midbottom=(212.5, 525))
            self.piao8_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_branco.png')
            self.piao8_rect = self.piao8_supr.get_rect(midbottom=(212.5, 600))

            # TORRES
            self.torre1_supr = pygame.image.load('Sprites/Pecas_Sprites/torre_branco.png')
            self.torre1_rect = self.torre1_supr.get_rect(midbottom=(137.5, 75))
            self.torre2_supr = pygame.image.load('Sprites/Pecas_Sprites/torre_branco.png')
            self.torre2_rect = self.torre2_supr.get_rect(midbottom=(137.5, 600))

            # CAVALOS
            self.cavalo1_supr = pygame.image.load('Sprites/Pecas_Sprites/cavalo_branco.png')
            self.cavalo1_rect = self.cavalo1_supr.get_rect(midbottom=(137.5, 150))
            self.cavalo2_supr = pygame.image.load('Sprites/Pecas_Sprites/cavalo_branco.png')
            self.cavalo2_rect = self.cavalo2_supr.get_rect(midbottom=(137.5, 525))

            # BISPOS
            self.bispo1_supr = pygame.image.load('Sprites/Pecas_Sprites/bispo_branco.png')
            self.bispo1_rect = self.bispo1_supr.get_rect(midbottom=(137.5, 225))
            self.bispo2_supr = pygame.image.load('Sprites/Pecas_Sprites/bispo_branco.png')
            self.bispo2_rect = self.bispo2_supr.get_rect(midbottom=(137.5, 450))

            # REI E RAINHA
            self.rei_supr = pygame.image.load('Sprites/Pecas_Sprites/rei_branco.png')
            self.rei_rect = self.rei_supr.get_rect(midbottom=(137.5, 300))
            self.rainha_supr = pygame.image.load('Sprites/Pecas_Sprites/rainha_branco.png')
            self.rainha_rect = self.rainha_supr.get_rect(midbottom=(137.5, 375))

        else:
            # PIÕES
            self.piao1_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao1_rect = self.piao1_supr.get_rect(midbottom=(587.5, 75))
            self.piao2_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao2_rect = self.piao2_supr.get_rect(midbottom=(587.5, 150))
            self.piao3_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao3_rect = self.piao3_supr.get_rect(midbottom=(587.5, 225))
            self.piao4_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao4_rect = self.piao4_supr.get_rect(midbottom=(587.5, 300))
            self.piao5_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao5_rect = self.piao5_supr.get_rect(midbottom=(587.5, 375))
            self.piao6_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao6_rect = self.piao6_supr.get_rect(midbottom=(587.5, 450))
            self.piao7_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao7_rect = self.piao7_supr.get_rect(midbottom=(587.5, 525))
            self.piao8_supr = pygame.image.load('Sprites/Pecas_Sprites/piao_preto.png')
            self.piao8_rect = self.piao8_supr.get_rect(midbottom=(587.5, 600))

            # TORRES
            self.torre1_supr = pygame.image.load('Sprites/Pecas_Sprites/torre_preto.png')
            self.torre1_rect = self.torre1_supr.get_rect(midbottom=(662.5, 75))
            self.torre2_supr = pygame.image.load('Sprites/Pecas_Sprites/torre_preto.png')
            self.torre2_rect = self.torre2_supr.get_rect(midbottom=(662.5, 600))

            # CAVALOS
            self.cavalo1_supr = pygame.image.load('Sprites/Pecas_Sprites/cavalo_preto.png')
            self.cavalo1_rect = self.cavalo1_supr.get_rect(midbottom=(662.5, 150))
            self.cavalo2_supr = pygame.image.load('Sprites/Pecas_Sprites/cavalo_preto.png')
            self.cavalo2_rect = self.cavalo2_supr.get_rect(midbottom=(662.5, 525))

            # BISPOS
            self.bispo1_supr = pygame.image.load('Sprites/Pecas_Sprites/bispo_preto.png')
            self.bispo1_rect = self.bispo1_supr.get_rect(midbottom=(662.5, 225))
            self.bispo2_supr = pygame.image.load('Sprites/Pecas_Sprites/bispo_preto.png')
            self.bispo2_rect = self.bispo2_supr.get_rect(midbottom=(662.5, 450))

            # REI E RAINHA
            self.rei_supr = pygame.image.load('Sprites/Pecas_Sprites/rei_preto.png')
            self.rei_rect = self.rei_supr.get_rect(midbottom=(662.5, 300))
            self.rainha_supr = pygame.image.load('Sprites/Pecas_Sprites/rainha_preto.png')
            self.rainha_rect = self.rainha_supr.get_rect(midbottom=(662.5, 375))

        self.pecas = [(self.piao1_supr, self.piao1_rect),
                      (self.piao2_supr, self.piao2_rect),
                      (self.piao3_supr, self.piao3_rect),
                      (self.piao4_supr, self.piao4_rect),
                      (self.piao5_supr, self.piao5_rect),
                      (self.piao6_supr, self.piao6_rect),
                      (self.piao7_supr, self.piao7_rect),
                      (self.piao8_supr, self.piao8_rect),
                      (self.torre1_supr, self.torre1_rect),
                      (self.torre2_supr, self.torre2_rect),
                      (self.cavalo1_supr, self.cavalo1_rect),
                      (self.cavalo2_supr, self.cavalo2_rect),
                      (self.bispo1_supr, self.bispo1_rect),
                      (self.bispo2_supr, self.bispo2_rect),
                      (self.rei_supr, self.rei_rect),
                      (self.rainha_supr, self.rainha_rect)]

    def validacao_E_selecao_peca(self, posicao_do_mouse): #Verifica se há uma colisão entre a posição do mouse e cada uma das peças do jogador. Caso colida a selecionada passa a ser essa.
        for peca in self.pecas:
            if peca[1].collidepoint(posicao_do_mouse) is True:
                self.peca_selecionada = (peca[0], peca[1])
                return True
        return False

    def existe_inimigo(self, rect):
        if self.existe_peca_no_quadrado((rect.x, rect.y)):
            if not self.peca_pertence_ao_jogador(rect):
                return True

    def espaco_valido_para_piao(self, rect_piao, rect_mover):
        #CASO SEJA BRANCO
        if self.cor == "BRANCO":

            #CASO AJA INIMIGO NAS DIAGONAIS
            if self.existe_inimigo_diagonal_cima(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x + 75, rect_piao.y - 75):
                    return True

            if self.existe_inimigo_diagonal_baixo(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x + 75, rect_piao.y + 75):
                    return True

            #CASO HAJA INIMIGO NA FRENTE
            if self.existe_inimigo_frente(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x + 75, rect_piao.y):
                    return False

            # CASO NÃO HAJA INIMIGO
            # CASO ESTEJA NA 2ª LINHA
            if rect_piao.x == 176:
                if not self.existe_inimigo_frente(rect_piao):
                    if (rect_piao.x + 75 == rect_mover.x and rect_piao.y == rect_mover.y):
                        return True
                    else:
                        if (rect_piao.x + 150 == rect_mover.x and rect_piao.y == rect_mover.y):
                            if not self.existe_inimigo_frente_X2(rect_piao):
                                return True

            # CASO NÃO ESTEJA
            if rect_piao.x + 75 == rect_mover.x and rect_piao.y == rect_mover.y:
                return True
            return False

        #CASO NÃO SEJA BRANCO
        else:
            #REPETE NO LADO INVERSO
            if self.existe_inimigo_diagonal_cima(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x - 75, rect_piao.y - 75):
                    return True
            if self.existe_inimigo_diagonal_baixo(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x - 75, rect_piao.y + 75):
                    return True
            if self.existe_inimigo_frente(rect_piao):
                if (rect_mover.x, rect_mover.y) == (rect_piao.x - 75, rect_piao.y):
                    return False
            if rect_piao.x == 551:
                if not self.existe_inimigo_frente(rect_piao):
                    if (rect_piao.x - 75 == rect_mover.x and rect_piao.y == rect_mover.y):
                        return True
                    else:
                        if (rect_piao.x - 150 == rect_mover.x and rect_piao.y == rect_mover.y):
                            if not self.existe_inimigo_frente_X2(rect_piao):
                                return True
            if rect_piao.x - 75 == rect_mover.x and rect_piao.y == rect_mover.y:
                return True
            return False
    def existe_peca_no_quadrado(self, rect_quadrado):
        for indice_quad in range(0, 64):
            #Verifica qual é o quadrado e quantas repetições levou a chegar a ele
            if (Jogo.lista_rect_tabuleiro[indice_quad].x, Jogo.lista_rect_tabuleiro[indice_quad].y) == rect_quadrado:
                if Jogo.mapa_pecas[indice_quad] is True:
                    return True
                return False
    def peca_pertence_ao_jogador(self, rect_peca):
        for peca in self.pecas:
            if peca == rect_peca:
                return True
        return False
    def existe_inimigo_diagonal_cima(self, rect_piao):
        if self.cor == 'BRANCO':
            if self.existe_peca_no_quadrado((rect_piao.x + 75, rect_piao.y - 75)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
        else:
            if self.existe_peca_no_quadrado((rect_piao.x + - 75, rect_piao.y - 75)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
    def existe_inimigo_diagonal_baixo(self, rect_piao):
        if self.cor == 'BRANCO':
            if self.existe_peca_no_quadrado((rect_piao.x + 75, rect_piao.y + 75)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
        else:
            if self.existe_peca_no_quadrado((rect_piao.x - 75, rect_piao.y + 75)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
    def existe_inimigo_frente(self, rect_piao):
        if self.cor == 'BRANCO':
            if self.existe_peca_no_quadrado((rect_piao.x + 75, rect_piao.y)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
        else:
            if self.existe_peca_no_quadrado((rect_piao.x - 75, rect_piao.y)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
    def existe_inimigo_frente_X2(self, rect_piao):
        if self.cor == 'BRANCO':
            if self.existe_peca_no_quadrado((rect_piao.x + 150, rect_piao.y)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True
        else:
            if self.existe_peca_no_quadrado((rect_piao.x - 150, rect_piao.y)):
                if not self.peca_pertence_ao_jogador(rect_piao):
                    return True

    def espaco_valido_para_torre(self, rect_torre, rect_mover):
        for espaco_valido in self.torre_rects_validos(rect_torre):
            if espaco_valido == (rect_mover.x, rect_mover.y):
                return True
    def torre_rects_validos(self, rect_torre):
        rects_possiveis = []

        # Verifica as linhas uma por uma e vai adicionando aos possiveis até que bata em um pião aliado ou inimigo (caso aliado não adiciona, caso inimigo adiciona aos rects possiveis e da break)
        for C in range(1, 8):
            if self.existe_peca_no_quadrado((rect_torre.x, rect_torre.y - 75 * C)):
                if self.peca_pertence_ao_jogador((rect_torre.x, rect_torre.y - 75 * C)):
                    break
                else:
                    rects_possiveis.extend([(rect_torre.x, rect_torre.y - 75 * C)])
                    break
            else:
                rects_possiveis.extend([(rect_torre.x, rect_torre.y - 75 * C)])

        for B in range(1, 8):
            if self.existe_peca_no_quadrado((rect_torre.x, rect_torre.y + 75 * B)):
                if self.peca_pertence_ao_jogador((rect_torre.x, rect_torre.y + 75 * B)):
                    break
                else:
                    rects_possiveis.extend([(rect_torre.x, rect_torre.y + 75 * B)])
                    break
            else:
                rects_possiveis.extend([(rect_torre.x, rect_torre.y + 75 * B)])

        for E in range(1, 8):
            if self.existe_peca_no_quadrado((rect_torre.x - 75 * E, rect_torre.y)):
                if self.peca_pertence_ao_jogador((rect_torre.x - 75 * E, rect_torre.y)):
                    break
                else:
                    rects_possiveis.extend([(rect_torre.x - 75 * E, rect_torre.y)])
                    break
            else:
                rects_possiveis.extend([(rect_torre.x - 75 * E, rect_torre.y)])

        for D in range(1, 8):
            if self.existe_peca_no_quadrado((rect_torre.x + 75 * D, rect_torre.y)):
                if self.peca_pertence_ao_jogador((rect_torre.x + 75 * D, rect_torre.y)):
                    break
                else:
                    rects_possiveis.extend([(rect_torre.x + 75 * D, rect_torre.y)])
                    break
            else:
                rects_possiveis.extend([(rect_torre.x + 75 * D, rect_torre.y)])

        return rects_possiveis


    def espaco_valido_para_cavalo(self, rect_cavalo, rect_mover):
        for espaco_valido in self.cavalo_rects_validos(rect_cavalo):
            if espaco_valido == (rect_mover.x, rect_mover.y):
                return True
    def cavalo_rects_validos(self, rect_cavalo):
        return [
            (rect_cavalo.x-150, rect_cavalo.y-75),
            (rect_cavalo.x-150, rect_cavalo.y+75),
            (rect_cavalo.x-75, rect_cavalo.y-150),
            (rect_cavalo.x-75, rect_cavalo.y+150),
            (rect_cavalo.x+150, rect_cavalo.y-75),
            (rect_cavalo.x+150, rect_cavalo.y+75),
            (rect_cavalo.x+75, rect_cavalo.y-150),
            (rect_cavalo.x+75, rect_cavalo.y+150)
        ]


    def espaco_valido_para_bispo(self, rect_bispo, rect_mover):
        for espaco_valido in self.bispo_rects_validos(rect_bispo):
            if espaco_valido == (rect_mover.x, rect_mover.y):
                return True
    def bispo_rects_validos(self, rect_bispo):
        rects_possiveis = []

        # Verifica as linhas uma por uma e vai adicionando aos possiveis até que bata em um pião aliado ou inimigo (caso aliado não adiciona, caso inimigo adiciona aos rects possiveis e da break)
        for EC in range(1, 8):
            if self.existe_peca_no_quadrado((rect_bispo.x - 75 * EC, rect_bispo.y - 75 * EC)):
                if self.peca_pertence_ao_jogador((rect_bispo.x - 75 * EC, rect_bispo.y - 75 * EC)):
                    break
                else:
                    rects_possiveis.extend([(rect_bispo.x - 75 * EC, rect_bispo.y - 75 * EC)])
                    break
            else:
                rects_possiveis.extend([(rect_bispo.x - 75 * EC, rect_bispo.y - 75 * EC)])

        for DC in range(1, 8):
            if self.existe_peca_no_quadrado((rect_bispo.x + 75 * DC, rect_bispo.y - 75 * DC)):
                if self.peca_pertence_ao_jogador((rect_bispo.x + 75 * DC, rect_bispo.y - 75 * DC)):
                    break
                else:
                    rects_possiveis.extend([(rect_bispo.x + 75 * DC, rect_bispo.y - 75 * DC)])
                    break
            else:
                rects_possiveis.extend([(rect_bispo.x + 75 * DC, rect_bispo.y - 75 * DC)])

        for EB in range(1, 8):
            if self.existe_peca_no_quadrado((rect_bispo.x - 75 * EB, rect_bispo.y + 75 * EB)):
                if self.peca_pertence_ao_jogador((rect_bispo.x - 75 * EB, rect_bispo.y + 75 * EB)):
                    break
                else:
                    rects_possiveis.extend([(rect_bispo.x - 75 * EB, rect_bispo.y + 75 * EB)])
                    break
            else:
                rects_possiveis.extend([(rect_bispo.x - 75 * EB, rect_bispo.y + 75 * EB)])

        for DB in range(1, 8):
            if self.existe_peca_no_quadrado((rect_bispo.x + 75 * DB, rect_bispo.y + 75 * DB)):
                if self.peca_pertence_ao_jogador((rect_bispo.x + 75 * DB, rect_bispo.y + 75 * DB)):
                    break
                else:
                    rects_possiveis.extend([(rect_bispo.x + 75 * DB, rect_bispo.y + 75 * DB)])
                    break
            else:
                rects_possiveis.extend([(rect_bispo.x + 75 * DB, rect_bispo.y + 75 * DB)])

        return rects_possiveis


    def espaco_valido_para_rei(self, rect_rei, rect_mover):
        for espaco_valido in self.rei_rects_validos(rect_rei):
            if espaco_valido == (rect_mover.x, rect_mover.y):
                return True
    def rei_rects_validos(self, rect_rei):
        return [
            (rect_rei.x, rect_rei.y - 75),
            (rect_rei.x, rect_rei.y + 75),
            (rect_rei.x - 75, rect_rei.y),
            (rect_rei.x + 75, rect_rei.y),
            # Diagonais
            (rect_rei.x - 75, rect_rei.y - 75),
            (rect_rei.x - 75, rect_rei.y + 75),
            (rect_rei.x + 75, rect_rei.y - 75),
            (rect_rei.x + 75, rect_rei.y + 75)
        ]


    def espaco_valido_para_rainha(self, rect_rainha, rect_mover):
        for espaco_valido in self.rainha_rects_validos(rect_rainha):
            if espaco_valido == (rect_mover.x, rect_mover.y):
                return True
    def rainha_rects_validos(self, rect_rainha):
        #Verifica cada pozição à volta, num raio de 7 espaços
        rects_possiveis = []

        # Verifica as linhas uma por uma e vai adicionando aos possiveis até que bata em um pião aliado ou inimigo (caso aliado não adiciona, caso inimigo adiciona aos rects possiveis e da break)
        for C in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x, rect_rainha.y - 75 * C)):
                if self.peca_pertence_ao_jogador((rect_rainha.x, rect_rainha.y - 75 * C)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x, rect_rainha.y - 75 * C)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x, rect_rainha.y - 75 * C)])

        for B in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x, rect_rainha.y + 75 * B)):
                if self.peca_pertence_ao_jogador((rect_rainha.x, rect_rainha.y + 75 * B)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x, rect_rainha.y + 75 * B)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x, rect_rainha.y + 75 * B)])

        for E in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x - 75 * E, rect_rainha.y)):
                if self.peca_pertence_ao_jogador((rect_rainha.x - 75 * E, rect_rainha.y)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x - 75 * E, rect_rainha.y)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x - 75 * E, rect_rainha.y)])

        for D in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x + 75 * D, rect_rainha.y)):
                if self.peca_pertence_ao_jogador((rect_rainha.x + 75 * D, rect_rainha.y)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x + 75 * D, rect_rainha.y)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x + 75 * D, rect_rainha.y)])

        for EC in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x - 75 * EC, rect_rainha.y - 75 * EC)):
                if self.peca_pertence_ao_jogador((rect_rainha.x - 75 * EC, rect_rainha.y - 75 * EC)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x - 75 * EC, rect_rainha.y - 75 * EC)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x - 75 * EC, rect_rainha.y - 75 * EC)])

        for DC in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x + 75 * DC, rect_rainha.y - 75 * DC)):
                if self.peca_pertence_ao_jogador((rect_rainha.x + 75 * DC, rect_rainha.y - 75 * DC)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x + 75 * DC, rect_rainha.y - 75 * DC)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x + 75 * DC, rect_rainha.y - 75 * DC)])

        for EB in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x - 75 * EB, rect_rainha.y + 75 * EB)):
                if self.peca_pertence_ao_jogador((rect_rainha.x - 75 * EB, rect_rainha.y + 75 * EB)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x - 75 * EB, rect_rainha.y + 75 * EB)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x - 75 * EB, rect_rainha.y + 75 * EB)])

        for DB in range(1, 8):
            if self.existe_peca_no_quadrado((rect_rainha.x + 75 * DB, rect_rainha.y + 75 * DB)):
                if self.peca_pertence_ao_jogador((rect_rainha.x + 75 * DB, rect_rainha.y + 75 * DB)):
                    break
                else:
                    rects_possiveis.extend([(rect_rainha.x + 75 * DB, rect_rainha.y + 75 * DB)])
                    break
            else:
                rects_possiveis.extend([(rect_rainha.x + 75 * DB, rect_rainha.y + 75 * DB)])

        return rects_possiveis


    def espaco_valido_para_peca(self, retangulo_da_peca, retangulo_para_mover):
        #CASO PECA SEJA PIAO
        if retangulo_da_peca == self.piao1_rect or retangulo_da_peca == self.piao2_rect or retangulo_da_peca == self.piao3_rect or retangulo_da_peca == self.piao4_rect or retangulo_da_peca == self.piao5_rect or retangulo_da_peca == self.piao6_rect or retangulo_da_peca == self.piao7_rect or retangulo_da_peca == self.piao8_rect:
            if self.espaco_valido_para_piao(retangulo_da_peca, retangulo_para_mover):
                return True
        #CASO PECA SEJA TORRA
        elif retangulo_da_peca == self.torre1_rect or retangulo_da_peca == self.torre2_rect:
            if self.espaco_valido_para_torre(retangulo_da_peca, retangulo_para_mover):
                return True
        #CASO PECA SEJA CAVALO
        elif retangulo_da_peca == self.cavalo1_rect or retangulo_da_peca == self.cavalo2_rect:
            if self.espaco_valido_para_cavalo(retangulo_da_peca, retangulo_para_mover):
                return True
        #CASO PECA SEJA BISPO
        elif retangulo_da_peca == self.bispo1_rect or retangulo_da_peca == self.bispo2_rect:
            if self.espaco_valido_para_bispo(retangulo_da_peca, retangulo_para_mover):
                return True
        #CASO PECA SEJA REI
        elif retangulo_da_peca == self.rei_rect:
            if self.espaco_valido_para_rei(retangulo_da_peca, retangulo_para_mover):
                return True
        #CASO PECA SEJA RAINHA
        elif retangulo_da_peca == self.rainha_rect:
            if self.espaco_valido_para_rainha(retangulo_da_peca, retangulo_para_mover):
                return True
        return False

    def consegue_mover(self, posicao_do_mouse):
        #percorro um loop e vejo se o mouse colide com algum dos retangulos dos quadrados todos do jogo
        pos_quadrado = 0
        for rect in Jogo.lista_rect_tabuleiro:
            if rect.collidepoint(posicao_do_mouse):
                #verificar se é um espaço movivel para peca atualmente selecionada
                if self.espaco_valido_para_peca(self.peca_selecionada[1], rect):
                    return True
        return False

    def not_piao(self, quadrado):
        if self.piao1_rect != quadrado and self.piao2_rect != quadrado and self.piao3_rect != quadrado and self.piao4_rect != quadrado and self.piao5_rect != quadrado and self.piao6_rect != quadrado and self.piao7_rect != quadrado and self.piao8_rect != quadrado:
            return True

    def mover_para_stack(self, sprite_peca, rect_peca):
        if self.cor == 'BRANCO':
            self.stack_ultima_peca.append((sprite_peca, (15, 20), rect_peca))
        else:
            self.stack_ultima_peca.append((sprite_peca, (715, 20), rect_peca))
        self.pos_ultima_peca += 1

    def alterar_pos_peca_original(self, rect_peca, rect_espaco_mover):
        if self.piao1_rect == rect_peca:
            self.piao1_rect = rect_espaco_mover
        elif self.piao2_rect == rect_peca:
            self.piao2_rect = rect_espaco_mover
        elif self.piao3_rect == rect_peca:
            self.piao3_rect = rect_espaco_mover
        elif self.piao4_rect == rect_peca:
            self.piao4_rect = rect_espaco_mover
        elif self.piao5_rect == rect_peca:
            self.piao5_rect = rect_espaco_mover
        elif self.piao6_rect == rect_peca:
            self.piao6_rect = rect_espaco_mover
        elif self.piao7_rect == rect_peca:
            self.piao7_rect = rect_espaco_mover
        elif self.piao7_rect == rect_peca:
            self.piao7_rect = rect_espaco_mover
        elif self.piao8_rect == rect_peca:
            self.piao8_rect = rect_espaco_mover
        elif self.torre1_rect == rect_peca:
            self.torre1_rect = rect_espaco_mover
        elif self.torre2_rect == rect_peca:
            self.torre2_rect = rect_espaco_mover
        elif self.cavalo1_rect == rect_peca:
            self.cavalo1_rect = rect_espaco_mover
        elif self.cavalo2_rect == rect_peca:
            self.cavalo2_rect = rect_espaco_mover
        elif self.bispo1_rect == rect_peca:
            self.bispo1_rect = rect_espaco_mover
        elif self.bispo2_rect == rect_peca:
            self.bispo2_rect = rect_espaco_mover
        elif self.rei_rect == rect_peca:
            self.rei_rect = rect_espaco_mover
        elif self.rainha_rect == rect_peca:
            self.rainha_rect = rect_espaco_mover
    def mover_peca(self, rect_peca, rect_local):
        #encontrar a peca na lista e trocala la dentro
        pos_peca = 0
        for peca in self.pecas:
            if peca[1] == rect_peca:
                #alterar peça original (graças ao mau design)
                self.alterar_pos_peca_original(rect_peca, rect_local)

                #alterar na lista de peças do jogador
                self.pecas[pos_peca] = (self.pecas[pos_peca][0], rect_local)
                self.peca_selecionada = self.pecas[pos_peca]
            pos_peca += 1

    def trocar_rect_com_piao(self, rect_piao, rect_peca_revivida):
        rect_novo = None

        #procurar o piao para pegar o rect dele e alterar o original para (0, 0)
        if rect_piao == self.piao1_rect:
            rect_novo = self.piao1_rect
            self.piao1_rect = (0, 0)
        if rect_piao == self.piao2_rect:
            rect_novo = self.piao2_rect
            self.piao2_rect = (0, 0)
        if rect_piao == self.piao3_rect:
            rect_novo = self.piao3_rect
            self.piao3_rect = (0, 0)
        if rect_piao == self.piao4_rect:
            rect_novo = self.piao4_rect
            self.piao4_rect = (0, 0)
        if rect_piao == self.piao5_rect:
            rect_novo = self.piao5_rect
            self.piao5_rect = (0, 0)
        if rect_piao == self.piao6_rect:
            rect_novo = self.piao6_rect
            self.piao6_rect = (0, 0)
        if rect_piao == self.piao7_rect:
            rect_novo = self.piao7_rect
            self.piao7_rect = (0, 0)
        if rect_piao == self.piao8_rect:
            rect_novo = self.piao8_rect
            self.piao8_rect = (0, 0)

        #procurar a peça para atribuir o rect do piao
        if rect_peca_revivida == self.torre1_rect:
            self.torre1_rect = rect_novo
        if rect_peca_revivida == self.torre2_rect:
            self.torre2_rect = rect_novo
        if rect_peca_revivida == self.cavalo1_rect:
            self.cavalo1_rect = rect_novo
        if rect_peca_revivida == self.cavalo2_rect:
            self.cavalo2_rect = rect_novo
        if rect_peca_revivida == self.bispo1_rect:
            self.bispo1_rect = rect_novo
        if rect_peca_revivida == self.bispo2_rect:
            self.bispo2_rect = rect_novo
        if rect_peca_revivida == self.rei_rect:
            self.rei_rect = rect_novo
        if rect_peca_revivida == self.rainha_rect:
            self.rainha_rect = rect_novo

    def reviver(self):
        #subtituo a peça do stack pela do pião
        if self.pos_ultima_peca == -1:
            return
        pos_peca = 0
        for peca in self.pecas:
            if peca == self.peca_selecionada:
                self.pecas[pos_peca] = (self.stack_ultima_peca[self.pos_ultima_peca][0], self.pecas[pos_peca][1])

                #O retangulo da peça revivida (torre, cavalo, etc) tem que receber o retangulo do pião que estava lá, para saber que ali é uma torre/etc e o rentangulo do pião recebe o da torre...
                self.trocar_rect_com_piao(self.pecas[pos_peca][1], self.stack_ultima_peca[self.pos_ultima_peca][2])
            pos_peca += 1

        #adiciono devolta à lista de peças
        self.pos_ultima_peca -= 1
        self.stack_ultima_peca.pop()

    def adicionar_na_espera(self, peca):
        self.lista_espera.extend([peca])
    def remover_da_espera(self):
        return self.lista_espera.pop(0)

    def existe_rei(self):
        for peca in self.pecas:
            if peca[1] == self.rei_rect:
                return True
        return False

    def load_tela_vencedor(self, tela):
        pygame.display.update()
        letras1_format = pygame.font.Font('Sprites/letras.ttf', 65)
        letras2_format = pygame.font.Font('Sprites/letras.ttf', 100)
        txt1_supr = letras1_format.render("Pressione  Espaco  Para  Sair", True, "Black")
        txt1_rect = txt1_supr.get_rect(center=(400, 500))
        txt2_supr = letras2_format.render(f"{self.nome}  Vence  !!!", True, "Black")
        txt2_rect = txt2_supr.get_rect(center=(400, 100))
        taca_supr = pygame.image.load('Sprites/Pecas_Sprites/trofeu.png')
        taca_rect = taca_supr.get_rect(center=(400, 300))
        fundo_supr = pygame.image.load('Sprites/Pecas_Sprites/Mesa.png')
        fundo_rect = fundo_supr.get_rect(topleft=(0, 0))
        sprites = [(fundo_supr, fundo_rect), (txt1_supr, txt1_rect), (txt2_supr, txt2_rect), (taca_supr, taca_rect)]
        for sprite in sprites:
            tela.blit(sprite[0], sprite[1])

