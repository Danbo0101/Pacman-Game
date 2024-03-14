
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


	matrix3=[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,3,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,3,1],
		[1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
		[1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1],
		[1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1],
		[1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1],
		[1,3,0,0,3,1,3,0,3,0,1,0,3,0,3,1,3,0,0,3,1],
		[1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1],
		[9,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,9],
		[0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0],
		[3,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,3],
		[0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0],
		[0,0,3,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,3,0,0],
		[1,1,0,0,3,1,0,0,0,9,0,9,0,0,0,1,3,0,0,1,1],
		[0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0],
		[0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0],
		[0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0],
		[3,0,3,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,3,0,3]

	]
	# matrix3=[
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

	screen = pygame.display.set_mode((KTI*len(matrix3[0]), KTI*len(matrix3))) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	
	font_bg=pygame.font.SysFont('vnibendigo',80)
	font_score=pygame.font.SysFont('gabriola',40)
	soundstart=pygame.mixer.Sound("sound/Pacman.ogg")
	soundstart.play()

	bg_win=pygame.transform.scale(pygame.image.load("background/bg4.png"),(700,438))

	map0 = BanDo(matrix3, KTI)
	"""
	slime0=Slime('character/inky.png',1,1,map0)
	slime1=Slime('character/inky.png',9,1,map0)
	slime2=Slime('character/Pinky.png',10,6,map0)
	slime3=Slime('character/Pinky.png',9,13,map0)
	slime4=Slime('character/Clyde.png',1,13,map0)
	slime5=Slime('character/Clyde.png',0,3,map0)
	slime6=Slime('character/Clyde.png',0,10,map0)
	"""
	slime0=Slime('character/inky.png',4,4,map0,6)
	slime1=Slime('character/inky.png',4,17,map0,6)
	slime2=Slime('character/Pinky.png',15,7,map0,6)
	slime3=Slime('character/Pinky.png',15,13,map0,6)
	slime4=Slime('character/Clyde.png',8,2,map0,6)
	slime5=Slime('character/Clyde.png',8,18,map0,6)
	slime6=Slime('character/xl.png',10,10,map0,8)
	#slime7=Slime(4,11,map0)
	

	tupSlime=(slime0,slime1,slime2,slime3,slime4,slime5,slime6)
	#tupSlime=()
	pacman=Pacman(16,10, map0,points,12)
	#pacman=Pacman(1,1, map0,points,15)
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
			label=font_bg.render("Score: "+ str(pacman.point + tong),True,(0,0,0))


			file_object=open("rank.txt","a").writelines(str(pacman.point+tong)+"\n")
			screen=pygame.display.set_mode((1000,638))
			screen.fill(WHITE)
			screen.blit(bg_win,(150,100))
			screen.blit(label,(350,460))
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