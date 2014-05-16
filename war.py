# Python 3.x
# War -- war.py
# v0.16

# A python replication of the War cardgame. It's also a learning 
# exercise for me to learn how object classes work.

from random import shuffle
class deck:
	def __init__(self,pool):
		self.pack=pool
	def draw(self):
		try: return self.pack.pop(0)
		except IndexError: return None
	def reset(self):
		self.pack=[]
	def take(self,pool,shuf=True):
		if shuf==True:shuffle(pool)
		self.pack+=pool
def war():
	pot.take([a.draw(),b.draw(),a.draw(),b.draw()],False)#a and b play 1 facedown card, then 1 faceup card
	if None not in pot.pack: compare()
def compare():
	if pot.pack[-2]>pot.pack[-1]: #if a>b...
		a.take(pot.pack)		#a gets the pot
	elif pot.pack[-2]<pot.pack[-1]:	#if a<b...
		b.take(pot.pack)			#b gets the pot
	else: war()	#else (a==b), war
	pot.reset()
def run():
	turn=0
	while len(a.pack) and len(b.pack):
		pot.take([a.draw(),b.draw()],False)
		compare()
		turn+=1
	print(turn)
	return turn
cards=[i for i in range(13)]*4
ttl=0
for i in range(999):
	shuffle(cards)
	a=deck(cards[:26])
	b=deck(cards[26:])
	pot=deck([])
	ttl+=run()
print(ttl/(i+1))
	