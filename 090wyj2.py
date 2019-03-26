#头像反弹

import pygame #导入pygame
pygame.init() #初始化 
screen=pygame.display.set_mode((850,650))#设置窗体大小（列表/列表）
pygame.display.set_caption("090wyj2")#设置标题
#设置屏幕颜色
YELLOW=(128,128,128)
screen.fill(YELLOW)

pic=pygame.image.load("wyj.jpg")
picx=0
picy=0
stepx=0.5
stepy=0.5
screen.blit(pic,(0,0))
picrect=pic.get_rect()
pich=picrect.height
picw=picrect.width


#主循环
keep_going=True
while keep_going:
    #获取事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    
    picx+=stepx
    picy+=stepy
    if picy+pich>=650 or picy<=0:
        stepy=-stepy
    if picx+picw>=850 or picx<=0:
        stepx=-stepx


    screen.fill(YELLOW)
    screen.blit(pic,(picx,picy))
    
    #更新屏幕
    pygame.display.update()

#结束
pygame.quit()
