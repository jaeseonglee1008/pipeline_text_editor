# (1)	cmd_h:  move cursor one character to the left 
# (2)	cmd_I:   move cursor one character to the right
# (3)	cmd_j: move cursor vertically one line up
# (4)	cmd_k: move cursor vertically one line down
# (5)	cmd_X: delete the character to the left of the cursor
# (6)	cmd_D: remove on current line from cursor to the end
# (7)	cmd_dd: delete current line and move cursor to the beginning of next line (if next line exists, else do nothing)
# (8)	cmd_ddp: transpose two adjacent lines
# (9)	cmd_n:   search for next occurrence of a string (assume that string to be searched is fully in one line.
# (10)	cmd_wq: write your representation as text file and save it

# For testing, you will read the following “nerdy” poem (from the “Zen of Python”) into your “file representation”. 

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.


import sys


class Command:
	"""docstring for Command"""
	def __init__(self, m, c, h):
		# super(Command, self).__init__()
		self.msg = m
		self.cursor = c
		self.horn = h

	def cmd_h(self):
		if self.cursor > 0:
			self.cursor -= 1
			print(self.cursor)
		print(self.display())

	def cmd_I(self):
		if self.cursor  < len(self.msg):
			self.cursor += 1
			print(self.cursor)
		print(self.display())


	def cmd_j(self):
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		for self.x in self.temp[0: len(self.temp)]:
			self.prev = self.count
			self.count 

		print(self.display())

	def cmd_k(self):
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		for self.x in self.temp[0:len(self.temp)-1]:
				self.prev = self.count
				self.count += len(self.x) + 1
				if self.count > self.cursor and self.count<len(self.msg):
					self.point = self.count - self.cursor
					self.cursor = self.prev + self.point
				else:
					self.cursor = len(self.msg)
		print(self.display())

	def cmd_X(self):
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		for self.x in self.temp[]

		print(self.display())

	def cmd_D(self):
		
		print(self.display())

	def cmd_dd(self):
		
		print(self.display())

	def cmd_ddp(self):
		
		print(self.display())

	def cmd_n(self):
		
		print(self.display())

	def cmd_wq(self):
		
		print(self.display())

	def display(self):
		self.temp = self.msg[0:self.cursor] + self.horn + self.msg[self.cursor :]
		return self.temp


def main():
	inst = """(1)cmd_h(or left):\tmove cursor one character to the left 
(2)cmd_I(or right):\tmove cursor one character to the right
(3)cmd_j(or v_up):\tmove cursor vertically one line up
(4)cmd_k(or v_down):\tmove cursor vertically one line down
(5)cmd_X(or del):\tdelete the character to the left of the cursor
(6)cmd_D(or del_right):\tremove on current line from cursor to the end
(7)cmd_dd(or del_line):\tdelete current line and move cursor to the beginning of
\t\t\tnext line (if next line exists, else do nothing)
(8)cmd_ddp(or trans):\ttranspose two adjacent lines
(9)cmd_n(or search):\tsearch for next occurrence of a string (assume that string
\t\t\tto be searched is fully in one line.
(10)cmd_wq(or save):\twrite your representation as text file and save it
(11)exit(or exit()):\tTerminate program
"""
	print(inst)
	horn = '^'
	cursor = 0
	msg = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""
	msg = """abcde
k123"""
	
	print(msg[0: cursor] + horn + msg[cursor: ])
	curr_msg = Command(msg, cursor, horn)
	# print(curr_msg.display())


	while True:
		try:
			cmd = input("Please enter your command: ")
			if cmd == "cmd_h" or cmd == "l":
				curr_msg.cmd_h()
			elif cmd == "cmd_I" or cmd == "r":
				curr_msg.cmd_I()
			elif cmd == "cmd_j" or cmd =="u":
				curr_msg.cmd_j()
			elif cmd == "cmd_k" or cmd =="d":
				curr_msg.cmd_k()
			elif cmd == "cmd_X" or cmd =="del":
				curr_msg.cmd_X()
			elif cmd == "cmd_D" or cmd == "del_right":
				curr_msg.cmd_D()
			elif cmd == "cmd_dd" or cmd == "del_line":
				curr_msg.cmd_dd()
			elif cmd == "cmd_ddp" or cmd == "trans":
				curr_msg.cmd_ddp()
			elif cmd == "cmd_n" or cmd == "search":
				curr_msg.cmd_n()
			elif cmd == "cmd_wq" or cmd == "save":
				curr_msg.cmd_wq()
			elif cmd == "exit()" or cmd =="e":
				print("BYEEEE :D")
				exit()
			else:
				print("Invalid command!")
		except IOError:
			continue


				






if __name__ == '__main__':
	main()
