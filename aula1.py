import pygame


def main():
  #As definições do objeto
        pygame.init()
        tela = pygame.display.set_mode([300, 300])
        pygame.display.set_caption("Iniciando o pygame")
        relogio = pygame.time.Clock()
        cor_branco = (255,255,255)
        cor_azul = (108,194,236)
        cor_verde = (152,231,114)
        cor_vermelho = (227,57,9)
        sup = pygame.Surface((200,200))
        sup.fill(cor_azul)

        sup2 = pygame.Surface((100,100))
        sup2.fill(cor_verde)

        ret = pygame.Rect(10,10,45,45)
        ret2 = pygame.Rect(50,50,100,60)
        pos = (30,30)
        circle2 = ((0,0),35)

        
        sair = False

        #inicializando fontes
        pygame.font.init()
        #criando variavei para armazenar a fonte padrao do sistema
        font_padrao = pygame.font.get_default_font()
        font_perdeu = pygame.font.SysFont(font_padrao, 45)
        font_ganhou = pygame.font.SysFont(font_padrao, 30)

        #variavel para armazenar arquivo de audio 
        audio_explosao = pygame.mixer.Sound('explosion-02.ogg')
        

        while sair != True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  
                  sair = True 

                if event.type == pygame.MOUSEBUTTONDOWN:
                  pygame.mouse.set_pos(150, 150)
                #if event.type == pygame.MOUSEMOTION:
                  #ret = ret.move(-10,-10)
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                        ret.move_ip(-10, 0)
                  if event.key == pygame.K_RIGHT:
                        ret.move_ip(10, 0)
                  if event.key == pygame.K_UP:
                        ret.move_ip(0, -10)
                  if event.key == pygame.K_DOWN:
                        ret.move_ip(0, 10)

          relogio.tick(30)
          tela.fill(cor_branco)
          tela.blit(sup, [50,50])
          tela.blit(sup2, [70,70])

          (xant, yant) = (ret.left, ret.top)
          (ret.left, ret.top) = pygame.mouse.get_pos()
          ret.left -= ret.width/2
          ret.top -= ret.height/2
          if ret.colliderect(ret2):
              #Renderizar o texto na tela quando houver coliusao, paramestro (texto, exibir, cor)  
              text = font_perdeu.render('COLIDIU', 1, (255, 255, 255))
              #Inserir o text na tela
              tela.blit(text, (150, 150))
              #play no audio
              audio_explosao.play()
              (ret.left,ret.top) = (xant, yant)

          pygame.draw.rect(tela, cor_vermelho, ret)
          pygame.draw.rect(tela, (253,147,226), ret2)
          pygame.draw.circle(tela, cor_verde, pos, 50)
          pygame.display.update()

          if pos < (200,200):
                y = 30
                y += 1
                pos = (y,30)
                        
                           
                
        

        pygame.quit() 

main()

