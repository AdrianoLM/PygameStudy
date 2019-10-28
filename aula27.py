import pygame


def main():
  #As definições do objeto
        pygame.init()

        #definindop o tamanho tela
        tela = pygame.display.set_mode([600, 450])
        pygame.display.set_caption("Iniciando o pygame")
        relogio = pygame.time.Clock()

        cor_branco = (255,255,255)
        cor_azul = (108,194,236)
        cor_verde = (152,231,114)
        cor_vermelho = (227,57,9)
        cor_preto = (0,0,0)

        #criando a superficie azul
        sup = pygame.Surface((600,450))
        sup.fill(cor_azul)

  

        #criando retangulo vemelho e o rosa
        ret = pygame.Rect(10,10,30,30)
        ret2 = pygame.Rect(0,70,555,6)
        ret3 = pygame.Rect(0,120,350,6)
        ret4 = pygame.Rect(405,120,195,6)
        ret5 = pygame.Rect(45,170,555,6)
        ret6 = pygame.Rect(0,220,350,6)
        ret7 = pygame.Rect(405,220,195,6)
        ret8 = pygame.Rect(0,270,555,6)
        ret9 = pygame.Rect(45,320,555,6)
        
        pos = (30,30)

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

                #Clicar com o mouse:  
                if event.type == pygame.MOUSEBUTTONDOWN:
                  pygame.mouse.set_pos(10, 10)
                  main()      
                  
              	#movimentação pro seta(não utilizado)
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                        ret.move_ip(-10, 0)
                  if event.key == pygame.K_RIGHT:
                        ret.move_ip(10, 0)
                  if event.key == pygame.K_UP:
                        ret.move_ip(0, -10)
                  if event.key == pygame.K_DOWN:
                        ret.move_ip(0, 10)
                  

          relogio.tick(60)
          tela.fill(cor_branco)

          #blitando a superficie azul na tela
          tela.blit(sup, [0,0])

          #variavel que armazena posição anterior do ret
          (xant, yant) = (ret.left, ret.top)

          #duas variaveis que definem a posição de ret recebem a posicao do mouse(/2 para ficar centralizado no ponteiro)
          (ret.left, ret.top) = pygame.mouse.get_pos()
          ret.left -= ret.width/2
          ret.top -= ret.height/2

          #verifica se houve colisão de ret com ret2
          if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(ret6) or ret.colliderect(ret7) or ret.colliderect(ret8) or ret.colliderect(ret9):
              
              #Renderizar o texto na tela quando houver colisão, parâmetro (texto, exibir, cor)  
              text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
              tela.blit(text, (215, 190))

              #volta para a posição inicial
              pygame.mouse.set_pos(10,10)

              #play no audio
              audio_explosao.play()

              #teleporta o ret para a posicão anterior a colisão
              (ret.left,ret.top) = (xant, yant)
          
          #se o ret estiver no alto da tela o ret2 volta para o lugar 
          if ret.top <50:
                ret2.left = 0

          #se o ret chegar em >400 ele ganha      
          if ret.top > 320:
                text = font_ganhou.render('GANHOU', 1, (255, 255, 255))
                tela.blit(text, (250, 200))
                text = font_ganhou.render('Clique para recomeçar', 1, (cor_vermelho))
                tela.blit(text, (185, 250))
                 #movendo ret2 para fora da tela
                ret2.left = 602
                ret3.left = 602
                ret4.left = 602
                ret5.left = 602
                ret6.left = 602
                ret7.left = 602
                ret8.left = 602
                ret9.left = 602

          pygame.draw.rect(tela, cor_vermelho, ret)
          pygame.draw.rect(tela, (253,147,226), ret2)
          pygame.draw.rect(tela, (253,147,226), ret3)
          pygame.draw.rect(tela, (253,147,226), ret4)
          pygame.draw.rect(tela, (253,147,226), ret5)
          pygame.draw.rect(tela, (253,147,226), ret6)
          pygame.draw.rect(tela, (253,147,226), ret7)
          pygame.draw.rect(tela, (253,147,226), ret8)
          pygame.draw.rect(tela, (253,147,226), ret9)
          pygame.display.update()

          if pos < (200,200):
                y = 30
                y += 1
                pos = (y,30)
                        
                           
                
        

        pygame.quit() 

main()
