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

#author : Jaeseong Lee(iamjason@bu.edu) hw7

import sys
import os


class Command:
	"""docstring for Command"""
	def __init__(self, m, c, h): #done
		# super(Command, self).__init__()
		self.msg = m
		self.cursor = c
		self.horn = h

	def cmd_h(self):#done
		if self.cursor > 0:
			self.cursor -= 1
			# print(self.cursor)
		print(self.display())

	def cmd_I(self):#done
		if self.cursor < len(self.msg):
			self.cursor += 1
			# print(self.cursor)
		print(self.display())

	def cmd_j(self): #done
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		self.line = 0

		for self.x in range(len(self.temp)):
			self.count -= len(self.temp[self.x]) + 1
			if self.count < 0:
				self.count += len(self.temp[self.x]) + 1
				self.line = self.x
				break
		#self.count = gap
		#self.line = line index
		if self.line > 0 and self.line < len(self.temp):
			self.cursor -= len(self.temp[self.line-1]) + 1
		print(self.display())

	def cmd_k(self):#done
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		self.line = 0

		for self.x in range(len(self.temp)):
			self.count -= len(self.temp[self.x]) + 1
			if self.count < 0:
				self.count += len(self.temp[self.x]) + 1
				self.line = self.x
				break
		#self.count = gap
		#self.line = line index
		if self.line < len(self.temp) and self.line<len(self.temp) -1:
			self.cursor += len(self.temp[self.line]) + 1

		print(self.display())

	def cmd_X(self):#done
		self.temp = list(self.msg)
		if self.cursor > 0:
			self.cursor -= 1
			self.temp.pop(self.cursor)
			self.msg = ''.join(self.temp)
		print(self.display())

	def cmd_D(self): #done

		self.temp = list(self.msg)
		self.check = self.temp[self.cursor:]
		# print(self.temp)
		if '\n' in self.check:
			self.x = self.temp.index('\n',self.cursor)
			del self.temp[self.cursor:self.x]
		else:
			del self.temp[self.cursor:]
		self.msg = ''.join(self.temp)
		# print(self.cursor)
		
		print(self.display())

	def cmd_dd(self):#done
		# self.temp = self.msg.splitlines()
		# self.point = self.cursor
		# if len(self.temp) != 0:
		# 	if self.cursor < len(self.temp[0]) + 1:
		# 		del self.temp[0]
		# 	else:
		# 		for self.x in range(len(self.temp)):
		# 			self.point -= len(self.temp[self.x])
		# 			if ((self.point) < (len(self.temp[self.x]))):
		# 				del self.temp[self.x]
		# 				break
		# self.msg = '\n'.join(self.temp)
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		self.line = 0

		for self.x in range(len(self.temp)):
			self.count -= len(self.temp[self.x]) + 1
			if self.count < 0:
				self.count += len(self.temp[self.x]) + 1
				self.line = self.x
				break

		del self.temp[self.line]
		self.cursor -= self.count
		self.msg = '\n'.join(self.temp)



		print(self.display())

	def cmd_ddp(self):#done
		self.temp = self.msg.splitlines()
		self.count = self.cursor
		self.line = 0

		for self.x in range(len(self.temp)):
			self.count -= len(self.temp[self.x]) + 1
			if self.count < 0:
				self.count += len(self.temp[self.x]) + 1
				self.line = self.x
				break

		if self.line == 0 and len(self.temp) >1:
			self.str = self.temp[self.line]
			self.temp[self.line] = self.temp[self.line+1]
			self.temp[self.line +1] = self.str
		elif len(self.temp) > 1 and self.line > 0:
			self.str = self.temp[self.line]
			self.temp[self.line] = self.temp[self.line-1]
			self.temp[self.line -1] = self.str
		self.msg = '\n'.join(self.temp)



		print(self.display())

	def cmd_n(self, s):
		self.word = s
		# print(self.word)

		# self.temp = list(self.msg)
		# self.check = self.temp[self.cursor:]
		# # print(self.temp)
		# if self.word in self.check:
		# 	self.cursor = self.temp.index('\n',self.cursor)
		# self.msg = ''.join(self.temp)
		# # print(self.cursor)

		self.temp = self.msg.splitlines()
		self.count = self.cursor
		self.line = 0
		self.pos =0
		for self.x in range(len(self.temp)):
			self.count -= len(self.temp[self.x]) + 1
			# print(self.count)
			if self.count < 0:
				self.count += len(self.temp[self.x]) + 1
				# print(self.count)
				self.line = self.x
				break
		# print(self.line)
		# print(self.count)
		self.pos = self.temp[self.line].find(self.word, self.count, len(self.temp[self.line])-1)
		if self.pos >0:
			self.cursor = self.cursor - self.count + self.pos 
		print(self.display())

	def cmd_wq(self):#done
		with open("Output_wq.txt", "w") as text_file:
			text_file.write(self.msg)
		print("Output_wq.txt has been created in the same directory!")
		print(self.display())

	def display(self): #done
		self.temp = self.msg[0:self.cursor] + self.horn + self.msg[self.cursor :]
		return self.temp
#Question : cmd_wq: do i need to include ^ or not

def main():
	inst = """(1)cmd_h(or l): move cursor one character to the left 
(2)cmd_I(or r): move cursor one character to the right
(3)cmd_j(or u): move cursor vertically one line up
(4)cmd_k(or d): move cursor vertically one line down
(5)cmd_X(or del): delete the character to the left of the cursor
(6)cmd_D(or del_right): remove on current line from cursor to the end
(7)cmd_dd(or del_line): delete current line and move cursor to the beginning of
\t\t\tnext line (if next line exists, else do nothing)
(8)cmd_ddp(or trans):transpose two adjacent lines
(9)cmd_n(ex: cmd_n(\"apple\")): search for next occurrence of a string (assume that string
\t\t\tto be searched is fully in one line.
(10)cmd_wq(or save): write your representation as text file and save it
(11)exit(or exit()): Terminate program
"""
	print("{}Command{}".format('='*20,'='*20))
	print(inst)
	print("{}Command{}".format('='*20,'='*20))
	horn = '^'
	cursor = 0
	nerdy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""



	outfile = open('nerdy.txt','w')
	outfile.write(nerdy)
	outfile.close()
	print("nerdy.txt has been created")

	__location__ = os.path.realpath(os.getcwd())

	while True:
		try:
			f_name = input("enter a file name in same directory (ex: nerdy.txt):")
			f_loc = os.path.join(__location__, f_name)
			f = open(os.path.join(__location__, f_name),"r+")
		except IOError:
			print("No file exist!")
			continue
		break
	# print("This is f")
	# print(f_loc)
	msg = str(f.read())
	print("{}Here is context below{}".format('='*20,'='*20))
	# print(msg)

	print(msg[0: cursor] + horn + msg[cursor: ])
	curr_msg = Command(msg, cursor, horn)
	# print(curr_msg.display())


	while True:
		try:
			print()
			cmd = input("***Please enter your command: ")
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
			elif cmd[0:5] == "cmd_n" or cmd == "search":
				word = cmd[7:-2]
				curr_msg.cmd_n(word)
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
