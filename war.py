# Python 3.x
# War -- war.py
# v0.1

# A python replication of the War cardgame. It's also a learning 
# exercise for me to learn how object classes work.

from random import shuffle
class deck:
	def __init__(self,pool):
		self.pack=pool
	def draw(self):
		return self.pack.pop(0)
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
	# while a.pack and b.pack > 0
		#add the top cards to the pool
		#if a's card is higher than b's card, a's pack gets pot
		#if b's card is higher than a's (b wins), b's pack gets pot
		#else (cards are equal), war
		#pot.reset()
	turn+=1	#there is a scope issue here for some reason. I think I can only reference outside but cannot modify... read up on this.
	print(turn)

cards=[i for i in range(2,15)]*4
shuffle(cards)
a=deck(cards[:26])
b=deck(cards[26:])
pot=deck([])
turn=0
run()