
import pygame as pygame
import pygame




GREY = (150,150,150)
WHITE = (255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
DARKBLUE=(10,10,128)
GRAY=(128,128,128)
pygame.init()
CANH=1
MAUCHU=YELLOW
KTI=43 #kich thuoc cua 1 khoi, thay doi độ to nhỏ cua bản đồ
COCHU=KTI #kich thuoc dau cham
#KTNV=32
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576
DOLUI=10


COLOR_WALL = DARKBLUE 
COLOR_GROUND = BLACK 		
COLOR_ACTIVE=GRAY 

FONT = pygame.font.Font(None, COCHU)


# doi tuong square cung cap các pixel tren ban do co the tuỳ chỉnh màu sac va thay doi trang thai

class Square():


	def __init__(self, x, y, KTI, style):


		self.rect = pygame.Rect(x, y, KTI, KTI)#khai báo các khối 
		self.KTI=KTI#độ to nhỏ của khối
		self.style=style
		if style == 0 or style == 3 or style==9:#ba style chính để ăn điểm
			self.color = COLOR_GROUND
		elif style == 1:#style của tường
			self.color = COLOR_WALL
		elif style == 2:#sytle khi đi qua sẽ active ô đó và sẽ khiến cho điểm point trên ô đó mất đi
			self.color = COLOR_ACTIVE
		self.active = False



	def draw(self, screen):

		# Blit the rect.
		pygame.draw.rect(screen, self.color, self.rect)
		if self.active ==False:#nếu ô đó chưa được active thì sẽ vẽ theo các style được thiết lập trước
			if self.style==0:
				self.printTT(screen,".")
			elif self.style==3: 
				self.printTT(screen,"o")
			elif self.style==9:
				x,y=self.chuyenTT(DOLUI)
				y+=DOLUI+KTI/6
				pygame.draw.ellipse(screen,WHITE,[x,y,DOLUI*2,DOLUI*2])

	def chuyenTT(self, dolui=0):
		return self.rect.left+self.KTI/2-dolui,self.rect.top+self.KTI/2-COCHU/2


	def printTT(self, screen, noiDung):
		txt_surface = FONT.render(noiDung, True, MAUCHU)
		screen.blit(txt_surface, self.chuyenTT(COCHU/10))

	def isIn(self,x,y):
		
		return self.rect.x-CANH<x<self.rect.x+self.KTI+CANH and self.rect.y-CANH<y<self.rect.y+self.KTI+CANH


"""
	doi tuong ban do cung cap cac phuong thuc tao, sua, di chuyen den 1 toa do tren map và vẽ
	chỉ co ban do hinh vuong dc su dung, ko the co ban do hinh chu nhat
"""
class BanDo():

	def __init__(self, matran, KTI):
		
		self.matran = matran
		self.IPS = len(matran) #so hang 
		self.IPSR = len(matran[0]) #so cot
		self.KTI=KTI # kich thuoc 1 o
		
		self.end=0

		self.banDo=self.sinhBD(matran)

		

	def chuyen(self,x,y):
		return x*self.KTI,y*self.KTI


	def sinhBD(self,matran):
		img=[]
		for i in range(self.IPS):
			for j in range(self.IPSR):
				xij,yij=self.chuyen(i,j)
				tmp=Square(yij,xij,self.KTI,matran[i][j]) #sua cho nay doi cho xij,yij
				if matran[i][j]!=1:
					self.end+=1
				img.append(tmp)
		return img	


	def draw(self,screen):
		for i in range(self.IPS*self.IPSR):
				self.banDo[i].draw(screen)
	
	# def Sroce(self):
	# 	if self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active==False and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].style in (0,3):
	# 			self.pacman_sound.play()
	# 			self.point+=1
	# 			self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active=True
	# 			self.end+=1

	# 	elif self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active==False and self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].style==9:
	# 			self.pacman_sound.play()
	# 			self.point+=1
	# 			self.banDo.banDo[f2t1(self.banDo.IPSR,i,j)].active=True
	# 			self.bd=getNow()
	# 			self.end+=1


def f2t1(IPSR,i,j):
		return i*IPSR+j


def main():


# 0 la dat, 1 la tuong , 3 là ghost
	matrix1=[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
		[1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1],
		[1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1],
		[1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1],
		[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
		[1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1],
		[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
		[0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0],
		[0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0],
		[1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1],
		[0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],
		[1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1],
		[0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0],
		[0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0],
		[0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0],
		[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0]

	]


	global SCREEN_WIDTH, SCREEN_HEIGHT 
	SCREEN_WIDTH=KTI*len(matrix1[0])*1
	SCREEN_HEIGHT=KTI*len(matrix1)*1

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1 man hinh du lon de chua map và du thêm buffer 

	clock = pygame.time.Clock()

	map0 = BanDo(matrix1, KTI)

	print(map0.banDo[0].isIn(KTI-4,KTI-2)) 

	done = False

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True



		map0.draw(screen)
		for i in range(map0.IPS):
			for j in range(map0.IPSR):

				map0.banDo[f2t1(map0.IPSR,i,j)].printTT(screen,str(i)+" "+str(j))


		pygame.display.flip()
		clock.tick(25)



if __name__ == '__main__':
	main()
	pygame.quit()
