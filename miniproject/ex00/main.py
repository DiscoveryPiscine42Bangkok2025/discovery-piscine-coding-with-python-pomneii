#!/usr/bin/env python3

from checkmate import checkmate

def main():
	board = """\
	....
	....
	....\
	..P.\
	"""
	# board = """\
	# ..
	# .K\
	# """

	# board = """\
	# ..PK....
	# ..P...K.
	# ..PPP...
	# Q.......
	# ........
	# ........
	# ........
	# ........\
	# """
	checkmate(board)

if __name__ == "__main__":
	main()

# python3 main.py | cat -e