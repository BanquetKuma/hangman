Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Deck:
	def __init__(self):
		self.card=[]
		for i in range(2,15):
			for j in range(4):
				self.card.append(Card(i,j))

				
>>> 
>>> 
>>> from random import shuffle
>>> class Deck:
	def __init__(self):
		self.card=[]
		for i in range(2,15):
			for j in range(4):
				self.card.append(Card(i,j))
		shuffle(self.card)
	def rm_card(self):
		if len(self.card)==0:
			return self.card.pop()

		
>>> deck=Deck()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    deck=Deck()
  File "<pyshell#17>", line 6, in __init__
    self.card.append(Card(i,j))
NameError: name 'Card' is not defined
>>> 
>>> 
>>> from random import shuffle
>>> class Card:
	suits=["spades","hearts","diamonds","clubs"]
	values=["None","None","2","3","4","5","6","7","8","9","10"
		"Jack","Queen","King","Ace"]
	def __init__(self,v,s):
		"""スート（マーク）も値も整数です"""
		self.value=v
		self.suit=s
	def __lt__(self,c2):
		if self.value<c2.value:
			return True
		if self.value==c2.value:
			if self.suit<c2.suit:
				return True
		else:
			return False
		return False
	def __gt__(self,c2):
		if self.value>c2.value:
			return True
		if self.value==c2.value:
			if self.suit>c2.suit:
				return True
			else:
				return False
		return False
	def __repr__(self):
		v=self.values[self.value]+" of "\
		   self.suits[self.suit]
		
SyntaxError: invalid syntax
>>> class Card:
	suits=["spades","hearts","diamonds","clubs"]
	values=["None","None","2","3","4","5","6","7","8","9","10"
		"Jack","Queen","King","Ace"]
	def __init__(self,v,s):
		"""スート（マーク）も値も整数です"""
		self.value=v
		self.suit=s
	def __lt__(self,c2):
		if self.value<c2.value:
			return True
		if self.value==c2.value:
			if self.suit<c2.suit:
				return True
		else:
			return False
		return False
	def __gt__(self,c2):
		if self.value>c2.value:
			return True
		if self.value==c2.value:
			if self.suit>c2.suit:
				return True
			else:
				return False
		return False
	def __repr__(self):
		v=self.values[self.value]+" of "\
		   +self.suits[self.suit]

		
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
	shuffle(self.cards)
        def rem_card(self):
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
	shuffle(self.cards)def rem_card(self):
		
SyntaxError: invalid syntax
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
	shuffle(self.cards)
        def rem_card(self):
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
	shuffle(self.cards)
	def rem_card(self):
		if len(self.cards)==0:
			return
		else:
			return self.cards.pop()

		
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    class Deck():
  File "<pyshell#68>", line 7, in Deck
    shuffle(self.cards)
NameError: name 'self' is not defined
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
	        shuffle(self.cards)
	def rem_card(self):
		if len(self.cards)==0:
			return
		else:
			return self.cards.pop()
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Deck():
	def __init__(self):
		self.cards=[]
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i,j))
		shuffle(self.cards)
	def rem_card(self):
		if len(self.cards)==0:
			return
		else:
			return self.cards.pop()

		
>>> class Player:
	def __init__(self,name):
		self.wins=0
		self.card=None
		self.name=name

		
>>> class Game:
	def __init__(self):
		name1=input("プレイヤー１の名前：")
		name2=input("プレイヤー2の名前：")
		self.deck=Deck()
		self.p1=Player(name1)
		self.p2=Player(name2)
	def wins(self,winner):
		w="このラウンドは{}が勝ちました"
		w=w.format.(winner)
		
SyntaxError: invalid syntax
>>> class Game:
	def __init__(self):
		name1=input("プレイヤー１の名前：")
		name2=input("プレイヤー2の名前：")
		self.deck=Deck()
		self.p1=Player(name1)
		self.p2=Player(name2)
	def wins(self,winner):
		w="このラウンドは{}が勝ちました"
		w=w.format(winner)
		print(w)
	def draw(self,p1n,p2n,p1c,p2c):
		d="{}は{}、{}は{}を引きました"
		d=d.format(p1n,p1c,p2n,p2c)
		print(d)
	def player_game(self):
		cards=self.deck.cards
		print("戦争を始めます")
		while len(cards)>=2:
			m="qで終了、それ以外のキーでplay:"
			response=input(m)
			if response=="q":
				break
			p1c=self.deck.rem_card()
			p2c=self.deck.rem_card()
			p1n=self.p1.name
			p2n=self.p2.name
			self.draw(p1n,p2n,p1c,p2c)
			if p1c>p2c:
				self.p1.wins+=1
				self.wins(self.p1.name)
			else:
				self.p2.wins+=1
				self.wins(self.p2.name)

				
>>> class Game:
	def __init__(self):
		name1=input("プレイヤー１の名前：")
		name2=input("プレイヤー2の名前：")
		self.deck=Deck()
		self.p1=Player(name1)
		self.p2=Player(name2)
	def wins(self,winner):
		w="このラウンドは{}が勝ちました"
		w=w.format(winner)
		print(w)
	def draw(self,p1n,p2n,p1c,p2c):
		d="{}は{}、{}は{}を引きました"
		d=d.format(p1n,p1c,p2n,p2c)
		print(d)
	def player_game(self):
		cards=self.deck.cards
		print("戦争を始めます")
		while len(cards)>=2:
			m="qで終了、それ以外のキーでplay:"
			response=input(m)
			if response=="q":
				break
			p1c=self.deck.rem_card()
			p2c=self.deck.rem_card()
			p1n=self.p1.name
			p2n=self.p2.name
			self.draw(p1n,p2n,p1c,p2c)
			if p1c>p2c:
				self.p1.wins+=1
				self.wins(self.p1.name)
			else:
				self.p2.wins+=1
				self.wins(self.p2.name)
		win=self.winner(self.p1,self.p2)
		print("ゲーム終了、{}の勝利です！".format(win))
	def winner(self,p1,p2):
		if self.p1.wins>self.p2.wins:
			return self.p1.name
		if self.p1.wins<self.p2.wins:
			return self.p2.name
		else:
			print("引き分け！！")

			
>>> game=Game()
プレイヤー１の名前：翔
プレイヤー2の名前：彩
>>> game.player_game()
戦争を始めます
qで終了、それ以外のキーでplay:k
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    game.player_game()
  File "<pyshell#130>", line 28, in player_game
    self.draw(p1n,p2n,p1c,p2c)
  File "<pyshell#130>", line 14, in draw
    d=d.format(p1n,p1c,p2n,p2c)
TypeError: __str__ returned non-string (type NoneType)
>>> game.player_game()
戦争を始めます
qで終了、それ以外のキーでplay:q
引き分け！！
ゲーム終了、Noneの勝利です！
>>> game.player_game()

戦争を始めます
qで終了、それ以外のキーでplay:4
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    game.player_game()
  File "<pyshell#130>", line 28, in player_game
    self.draw(p1n,p2n,p1c,p2c)
  File "<pyshell#130>", line 14, in draw
    d=d.format(p1n,p1c,p2n,p2c)
  File "<pyshell#50>", line 29, in __repr__
    +self.suits[self.suit]
IndexError: list index out of range
>>> 
