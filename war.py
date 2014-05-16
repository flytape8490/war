# Python 3.x
# War -- war.py
# v0.15

# A python replication of the War cardgame. It's also a learning 
# exercise for me to learn how object classes work.

from random import shuffle
class deck:
	def __init__(self,pool):
		self.pack=pool
	def draw(self):
		return self.pack.pop(0)
		#add a try to figure out how to break when cards run out during war. Maybe return 'None' and add a ' if none in pack' statement?
	def reset(self):
		self.pack=[]
	def take(self,pool,shuf=True):
		if shuf==True:shuffle(pool)
		for i in pool:
			self.pack.append(i)
			
def war(): #[a1,b1,adown,bdown,aup,bup]  #-2=aup, -1=bup
	pot.take([a.draw(),b.draw(),a.draw(),b.draw()],False)
	if pot.pack[-2]>pot.pack[-1]:	#aup>bup
		for i in pot.pack:
			a.take(pot.pack)
	elif pot.pack[-2]<pot.pack[-1]:
			b.take(pot.pack)
	else:
		war()

def run():
	turn=0
	while len(a.pack) and len(b.pack):
		pot.take([a.draw(),b.draw()],False)
		if pot.pack[0]>pot.pack[1]: a.take(pot.pack)
		elif pot.pack[0]<pot.pack[1]: b.take(pot.pack)
		else: war()
		pot.reset()
		turn+=1
	print(turn)

cards=[i for i in range(2,15)]*4
shuffle(cards)
a=deck(cards[:26])
b=deck(cards[26:])
pot=deck([])
run()