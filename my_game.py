import pygame,sys,random
import time
pygame.init()

screen=pygame.display.set_mode((1000,700))

clock=pygame.time.Clock()
image1=pygame.image.load("back.png")
image1=pygame.transform.scale(image1,(1000,700))
target1=pygame.image.load("target.png")
target1_list=[]



game_font=pygame.font.Font(None,60)

cross_hair=pygame.image.load("circle21.png").convert_alpha()
cross_hair=pygame.transform.scale(cross_hair,(100,100))


score=0

j=1



while True:
    clock.tick(10)
    
    text1=game_font.render("SHOOT RED TARGETS",True,(random.randrange(0,255),0,0))
    l=50+j
    if l>=500:
        l=50

    screen.blit(image1,(0,0))
    for target in range(1):
      target1_position_x=random.randrange(50,800)
      target1_position_y=random.randrange(50,500)
      target1_rect=target1.get_rect(center=(target1_position_x,target1_position_y))
      target1_list.append(target1_rect)

    if len(target1_list) >5:
      target1_list=[]
    
  
    


    screen.blit(text1,(400,100))
    
        
    for target1_rect in target1_list:
      screen.blit(target1,target1_rect)




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            cross_rect=cross_hair.get_rect(center=event.pos)
        if event.type==pygame.MOUSEBUTTONDOWN:
          for index,target1_rect in enumerate(target1_list):
            if target1_rect.collidepoint(event.pos):

              del target1_list[index]
              score=score+1
              
          

    screen.blit(cross_hair,cross_rect )
    text2=game_font.render("Score="+str(score),True,(0,0,0))
    screen.blit(text2,(500,20))
    if score>30:
      break
    
                    

                    
            
        
    
    pygame.display.update()


image4=pygame.image.load("black.jpg")
image4=pygame.transform.scale(image4,(1000,700))
font12=pygame.font.Font(None,100)
text5=font12.render("YOU WIN",True,(215,190,105))

screen.blit(image4,(0,0))

for i in range(1000):
        text3=game_font.render(".",True,(215,190,105))
        
        screen.blit(text3,(random.randint(0,1000),random.randint(0,700)))
screen.blit(text5,(300,250))

pygame.display.update()
time.sleep(4)
for event in pygame.event.get():
  if event.type==pygame.QUIT:
    pygame.quit()
    sys.exit()
    
    

    


  
