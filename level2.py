
from pygame.font import Font
from Slime import Slime

from Char import Pacman
from BanDo import *
import pygame


def rapePM(pacman,slimeTup):
	for slime in slimeTup:
		if slime.rape(pacman):
			pacman.explosion=True
			
def rapeSlime(slime,pacman):
		if pacman.rape(slime):
			slime.explosion=True  
 
def main(points):
	pygame.init()


	matrix2=[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
		[1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1],
		[1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1],
		[1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1],
		[0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],
		[1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1],
		[9,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,9],
		[0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0],
		[0,0,0,0,1,0,1,9,0,0,0,0,0,9,1,0,1,0,0,0,0],
		[1,1,0,3,0,0,1,1,1,1,1,1,1,1,1,0,0,3,0,1,1],
		[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		[9,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,9],
		[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[1,1,0,0,0,0,3,1,1,1,1,1,1,1,3,0,0,0,0,1,1],
		[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
		[1,0,0,1,1,1,0,1,1,1,3,1,1,1,0,1,1,1,0,0,1],
		[1,3,0,0,0,0,3,1,0,0,0,0,0,1,3,0,0,0,0,3,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	]
	# matrix1=[
	# 	[1,1,1,1],
	# 	[1,0,0,1],
	# 	[1,0,0,1],
	# 	[1,1,1,1],
		

		
	# ]    

	RIGHT = 1073741903
	LEFT = 1073741904
	UP = 1073741906
	DOWN = 1073741905

	huong="s"

	screen = pygame.display.set_mode((KTI*len(matrix2[0]), KTI*len(matrix2))) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	
	font=pygame.font.SysFont('vnibendigo',80)
	font_score=pygame.font.SysFont('gabriola',40)
	soundstart=pygame.mixer.Sound("sound/Pacman.ogg")
	soundstart.play()

	bg_level_up=pygame.transform.scale(pygame.image.load("background/Level-up.png"),(700,438))

	map0 = BanDo(matrix2, KTI)
	
	slime0=Slime('character/inky.png',1,6,map0,4)
	slime1=Slime('character/inky.png',1,14,map0,4)
	slime2=Slime('character/Pinky.png',7,2,map0,4)
	slime3=Slime('character/Pinky.png',7,18,map0,4)
	slime4=Slime('character/Clyde.png',17,8,map0,4)
	slime5=Slime('character/Clyde.png',17,12,map0,4)
	#slime6=Slime('character/Clyde.png',0,10,map0,4)
	
	
	#slime7=Slime(4,11,map0)
	

	#tupSlime=(slime0,slime1,slime2,slime3,slime4,slime5,slime6)
	tupSlime=(slime0,slime1,slime2,slime3,slime4,slime5)
	#pacman=Pacman(7,10, map0,points,12)
	pacman=Pacman(9,10, map0,points,15)
	#pacman.point+=point1
	done = False

	while not done:

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				print("nhan",event.key)
				if event.key==RIGHT:
					huong="r"
				elif event.key==LEFT:
					huong="l"
				elif event.key==DOWN:
					huong="d"
				elif event.key==UP:
					huong="u"
				elif event.key == pygame.K_ESCAPE:
					done = True
		
		map0.draw(screen)
		labelS=font_score.render("Score: "+ str(pacman.point),True,(255,255,102))
		screen.blit(labelS,(10,10))

		
		for slime in tupSlime:
			slime.draw(screen)
			slime.update(pacman)
	
		
		

		pacman.draw(screen)
		pacman.update(huong,screen)


		
		rapePM(pacman,tupSlime)
		for slime in tupSlime:
			rapeSlime(slime,pacman)
		
		if pacman.game_over==True: 
			done=True
			points[0]=pacman.point
			return False
		if pacman.end==map0.end:
			
			tong=0
			for i in points:
				tong+=i
			label=font.render("Score: "+ str(pacman.point + tong),True,(0,0,0))
			screen=pygame.display.set_mode((1000,638))
			screen.fill(WHITE)
			screen.blit(bg_level_up,(150,50))
			screen.blit(label,(360,400))
			pygame.display.flip()
			pygame.time.wait(5000)
			done=True
			points[0]=pacman.point
			return True
			
		
    			

		pygame.display.flip()
		clock.tick(20)

    
if __name__ == '__main__':
	main(points=[0,0,0])
	pygame.quit()